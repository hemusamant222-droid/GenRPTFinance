import React from 'react';
import {AbsoluteFill, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';

export type DemoProps = {screenshot: string; headline: string};

// All motion is frame-driven so previews and renders are deterministic.
export const GenRPTFinanceDemo: React.FC<DemoProps> = ({screenshot, headline}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const entrance = spring({frame, fps, config: {damping: 200}});
  const outro = interpolate(frame, [405, 449], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const progress = interpolate(frame, [0, 449], [0, 100]);
  return (
    <AbsoluteFill style={{background: '#080e1d', color: '#f2f6ff', fontFamily: 'Arial, sans-serif', padding: '65px 90px', opacity: outro}}>
      <AbsoluteFill style={{background: 'radial-gradient(ellipse at 75% 35%, #133d47 0%, transparent 65%)'}} />
      <div style={{position: 'relative', display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
        <div style={{fontSize: 32, fontWeight: 700}}>GenRPT <span style={{color: '#66e8c1'}}>Finance</span></div>
        <div style={{fontSize: 17, letterSpacing: 4, color: '#9caec8'}}>PRODUCT WALKTHROUGH</div>
      </div>
      <div style={{position: 'relative', marginTop: 47, opacity: entrance, transform: `translateY(${(1 - entrance) * 30}px)`}}>
        <div style={{fontSize: 18, color: '#66e8c1', letterSpacing: 4, marginBottom: 18}}>A CLEARER VIEW OF YOUR FINANCES</div>
        <h1 style={{fontSize: 66, letterSpacing: -2, margin: 0, fontWeight: 600}}>{headline}</h1>
      </div>
      <div style={{position: 'relative', marginTop: 42, flex: 1, minHeight: 0, border: '1px solid #345064', borderRadius: 20, overflow: 'hidden', boxShadow: '0 25px 90px #0008', transform: `scale(${0.97 + entrance * 0.03})`, background: '#101c2e'}}>
        <div style={{height: 44, background: '#1a2a40', display: 'flex', alignItems: 'center', gap: 8, paddingLeft: 20}}>
          {['#f48e8e', '#e8cd82', '#66e8c1'].map(color => <div key={color} style={{width: 10, height: 10, borderRadius: '50%', background: color}} />)}
          <span style={{fontSize: 13, marginLeft: 18, color: '#9caec8'}}>GenRPT Finance · Product preview</span>
        </div>
        {screenshot ? <Img src={staticFile(screenshot)} style={{width: '100%', height: 'calc(100% - 44px)', objectFit: 'contain'}} /> : (
          <div style={{height: 'calc(100% - 44px)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 22}}>
            <div style={{fontSize: 54, color: '#66e8c1'}}>Your product. In focus.</div>
            <div style={{fontSize: 24, color: '#b5c5da'}}>Actual product screenshot goes here</div>
            <div style={{fontSize: 18, color: '#7f93af'}}>Add an image to public/screenshots and set the screenshot prop.</div>
          </div>
        )}
      </div>
      <div style={{position: 'relative', marginTop: 26, display: 'flex', justifyContent: 'space-between', color: '#a7b7ce', fontSize: 18}}>
        <span>GenRPT Finance</span><span>Product demo · 15 seconds</span>
      </div>
      <div style={{position: 'absolute', left: 0, bottom: 0, height: 4, width: `${progress}%`, background: '#66e8c1'}} />
    </AbsoluteFill>
  );
};
