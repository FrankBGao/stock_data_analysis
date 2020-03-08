import React from "react";
import {Card} from "antd";
import Stock from "./stock"

const Chart: React.FC<{}> = props => {


  return (
    <div>
      <Card>
        <Stock />
      </Card>

    </div>
  )
};

export default Chart;
