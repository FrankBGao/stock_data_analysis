import React from 'react';

import "@antv/graphin/dist/index.css";
import "@antv/graphin-components/dist/index.css";
import PageHeaderWrapper from "@ant-design/pro-layout/lib/PageHeaderWrapper";
import Heatmap from "./heatmap"
import Basic from "./multipleChart"

export default (): React.ReactNode => (
  <PageHeaderWrapper>
    {/*<Heatmap />*/}
    <Basic />
  </PageHeaderWrapper>

);
