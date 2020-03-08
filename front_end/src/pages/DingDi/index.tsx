import React from 'react';

import "@antv/graphin/dist/index.css";
import "@antv/graphin-components/dist/index.css";
import PageHeaderWrapper from "@ant-design/pro-layout/lib/PageHeaderWrapper";
import Chart from "./Chart"

export default (): React.ReactNode => (
  <PageHeaderWrapper>
    <Chart/>
  </PageHeaderWrapper>

);
