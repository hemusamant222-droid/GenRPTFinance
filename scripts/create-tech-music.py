"""Create an original, deterministic instrumental bed; no sampled recordings.
Run: python scripts/create-tech-music.py [output.wav]
"""
from pathlib import Path
import sys, wave
import numpy as np

SR, DURATION, BPM = 48000, 33, 112
rng = np.random.default_rng(42)
mix = np.zeros((SR * DURATION, 2), dtype=np.float64)
beat = 60 / BPM

def hz(note):
    return 440 * 2 ** ((note - 69) / 12)

def add(start, sound, gain=1, pan=0):
    offset = int(start * SR)
    count = min(len(sound), len(mix) - offset)
    if count <= 0:
        return
    angle = (pan + 1) * np.pi / 4
    mix[offset:offset+count, 0] += sound[:count] * gain * np.cos(angle)
    mix[offset:offset+count, 1] += sound[:count] * gain * np.sin(angle)

# Restrained harmonic pad: Am / F / C / Dm, two bars per chord.
chords = [[57,60,64,69], [53,57,60,65], [48,55,60,64], [50,57,62,65]]
for bar in range(16):
    start = bar * beat * 4
    chord = chords[(bar // 2) % 4]
    t = np.arange(int((beat * 4 + .6) * SR)) / SR
    env = np.minimum(t / .7, 1) * np.minimum(np.maximum(beat * 4 + .6 - t, 0) / .8, 1)
    for j, note in enumerate(chord):
        f = hz(note)
        tone = (np.sin(2*np.pi*f*t) + .2*np.sin(2*np.pi*(f*1.002)*t)) * env
        add(start, tone, .018, [-.6,-.2,.2,.6][j])

# Muted, stereo eighth-note arpeggio with two quiet delay taps.
for step in range(int(DURATION / (beat/2))):
    start = step * beat / 2
    chord = chords[(step // 16) % 4]
    note = chord[[0,2,1,3,2,1,3,2][step % 8]] + 12
    t = np.arange(int(.5 * SR)) / SR
    env = (1-np.exp(-t*230)) * np.exp(-t*12)
    tone = (np.sin(2*np.pi*hz(note)*t) + .12*np.sin(4*np.pi*hz(note)*t)) * env
    gain = .065 if step % 4 == 0 else .043
    pan = -.4 if step % 2 else .4
    add(start, tone, gain, pan)
    add(start+beat*.75, tone, gain*.22, -pan)
    add(start+beat*1.5, tone, gain*.09, pan)

for b in range(int(DURATION / beat)):
    start = b * beat
    chord = chords[(b // 8) % 4]
    # Short rounded bass pulse, below the harmonic bed.
    t = np.arange(int(.38 * SR)) / SR
    f = hz(chord[0]-12)
    bass = (np.sin(2*np.pi*f*t)+.16*np.sin(4*np.pi*f*t)) * (1-np.exp(-t*150))*np.exp(-t*9)
    add(start, bass, .11)
    if start > 2:
        # Soft kick, no aggressive transient.
        t = np.arange(int(.23 * SR)) / SR
        phase = 2*np.pi*(48*t + 45*.025*(1-np.exp(-t/.025)))
        add(start, np.sin(phase)*np.exp(-t*24), .14)
        # Brief filtered-noise tick on the offbeat.
        t = np.arange(int(.048 * SR)) / SR
        noise = rng.normal(0,1,len(t))
        tick = np.concatenate(([0], np.diff(noise))) * np.exp(-t*110)
        add(start+beat/2,tick,.010, .35 if b%2 else -.35)
        if b % 2:
            t = np.arange(int(.09 * SR)) / SR
            noise = rng.normal(0,1,len(t))
            noise = np.convolve(noise, np.ones(7)/7, mode='same')
            add(start,noise*np.exp(-t*55),.033,-.1)

# Smooth mastering and a musical tail, with silence at both ends.
t = np.arange(len(mix)) / SR
fade = np.minimum(t/1.1,1) * np.minimum(np.maximum(DURATION-t,0)/2.5,1)
mix *= fade[:, None]
mix = np.tanh(mix*1.8)
mix *= .68 / max(np.max(np.abs(mix)), 1e-9)
pcm = (mix * 32767).astype('<i2')
out = Path(sys.argv[1] if len(sys.argv)>1 else 'out/genrpt-tech-bed.wav')
out.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(out),'wb') as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes(pcm.tobytes())
print(f'Created {out}: {DURATION}s, stereo, {BPM} BPM')
