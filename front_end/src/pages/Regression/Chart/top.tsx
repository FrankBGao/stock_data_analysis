import ChartCard from '../ChartCard';
import Trend from '../Trend';
import React, {useState} from "react";
import { Card, Col, Row, Tooltip } from 'antd';
import { InfoCircleOutlined } from '@ant-design/icons';

interface TopProps {
  code:string,
  priceChange:string,
  earn:string,
  times:number
}


const Top: React.FC<TopProps> = props => {
  // const [state, setState] = useState({
  //   code:props.code,
  //   priceChange:props.priceChange,
  //   earn:props.earn,
  //   times:props.times
  // });

  return (
    <div>
      <Row gutter={24} type="flex">
        <Col xl={6} lg={12} md={24} sm={24} xs={24} style={{marginBottom: 24}}>
          <ChartCard
            bordered={false}
            title={
              "股票代码"
            }
            action={
              <Tooltip
                title={
                 "股票代码"
                }
              >
                <InfoCircleOutlined />
              </Tooltip>
            }
            total={() => <h3>{props.code}</h3>}

            contentHeight={46}
          >

          </ChartCard>
        </Col>
        <Col xl={6} lg={12} md={24} sm={24} xs={24} style={{marginBottom: 24}}>
          <ChartCard
            bordered={false}
            title={
              "股价浮动"
            }
            action={
              <Tooltip
                title={
                  "第一天的开盘价与最后一天的收盘价"
                }
              >
                <InfoCircleOutlined />
              </Tooltip>
            }
            total={() => <h3>{props.priceChange}%</h3>}

            contentHeight={46}
          >

          </ChartCard>
        </Col>
        <Col xl={6} lg={12} md={24} sm={24} xs={24} style={{marginBottom: 24}}>
          <ChartCard
            bordered={false}
            title={
              "收益率"
            }
            action={
              <Tooltip
                title={
                  "策略获得的收益"
                }
              >
                <InfoCircleOutlined />
              </Tooltip>
            }
            total={() => {return <div><h3>{props.earn}%</h3></div>}}

            contentHeight={46}
          >

          </ChartCard>
        </Col>
        <Col xl={6} lg={12} md={24} sm={24} xs={24} style={{marginBottom: 24}}>
          <ChartCard
            bordered={false}
            title={
              "交易次数"
            }
            action={
              <Tooltip
                title={
                  "策略在这段时间的交易次量"
                }
              >
                <InfoCircleOutlined />
              </Tooltip>
            }
            total={() => <h3>{props.times}</h3>}

            contentHeight={46}
          >

          </ChartCard>
        </Col>
      </Row>

    </div>
  )
};

export default Top;
