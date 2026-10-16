import React from 'react';
import {Composition} from 'remotion';
import {GenRPTFinanceDemo} from './GenRPTFinanceDemo';

export const RemotionRoot: React.FC = () => (
  <Composition id="GenRPTFinanceDemo" component={GenRPTFinanceDemo}
    durationInFrames={450} fps={30} width={1920} height={1080}
    defaultProps={{screenshot: '', headline: 'Financial clarity. In every report.'}} />
);
