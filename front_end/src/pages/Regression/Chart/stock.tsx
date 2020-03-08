import React, {useState} from "react";
import {Button, Modal, Input, Select, Card, Row, Col, Slider, InputNumber, Tabs ,message} from "antd";
import Basic from "./multipleChart";
import Curved from "./lineChart";
import TradeTable from "./tradeRecordTable";
import Top from "./top";
import Item from '../Item';

import service from "../Service"
// import {string} from "prop-types";

interface StockProps {

}

// interface StockState {
//   data: any
// }

let data = require("./result.json");
let tradeRecord = require("./trading_record.json");
let regress_result = require("./regress_result.json");

const Stock: React.FC<StockProps> = props => {
  const {Option} = Select;
  const {TabPane} = Tabs;

  const [state, setState] = useState({
    modalShow: false,
    code: "600030" as string,
    combineDingDi: true,
    adjustment: false,

    invest: 100000 as number,
    strategy: "complex" as string,
    up_threshold: 0.1 as number,
    down_threshold: 0.05 as number,
    safety_down: 0.2 as number,
    safety_up: 0.1 as number,
    initial_step: "normal" as string,
    cold_down_period: 30 as number,

  });

  const [v_state, v_setState] = useState({
    data: data as any,
    tradeRecord: tradeRecord as any,
    regress_result: regress_result as any,
  });
  const {up_threshold, down_threshold, safety_down, safety_up, initial_step, cold_down_period, strategy} = state;
  // ding di
  const InputCodeChange = (event: any) => {
    setState({...state, code: event.target.value})
  };

  const InputInvestChange = (event: any) => {
    setState({...state, invest: event.target.value})
  };

  const gainDingDi = async () => {
    const result = await service.queryRegression(state.code, {
      code: state.code,
      invest: state.invest,
      strategy: state.strategy,
      up_threshold: state.up_threshold,
      down_threshold: state.down_threshold,
      safety_down: state.safety_down,
      safety_up: state.safety_up,
      initial_step: state.initial_step,
      cold_down_period: state.cold_down_period,
    });
    console.log(result);
    setState({
      ...state,
      modalShow: false,
    });
    v_setState({
      ...v_state,
      data: JSON.parse(result["everyday_result"]),
      tradeRecord: JSON.parse(result["trading_record"]),
      regress_result: result["result"]
    });
  };

  const ModalOnOk = () => {
    gainDingDi().then();
  };

  const ModalOnCancel = () => {
    setState({...state, modalShow: false});
  };

  const ButtonOnClick = () => {
    setState({...state, modalShow: true});
  };

  const refreshData = async () => {
    await service.queryRefresh();
  };
  const ButtonRefreshOnClick = () => {
    refreshData().then();
    message.success("更新成功")
  };


  return (
    <div>
      <div style={{marginBottom: 20}}>
        <Button onClick={ButtonOnClick}type="danger">
          回测
        </Button>

        <Button type="danger" onClick={ButtonRefreshOnClick} style={{marginLeft:10}}>
          数据更新
        </Button>
      </div>
      <Top code={state.code}
           priceChange={((v_state.data[v_state.data.length - 1]["end"] - v_state.data[0]["start"]) * 100 / v_state.data[0]["start"]).toFixed(2)}
           earn={(v_state.regress_result["earn_percentage"] * 100).toFixed(2)}
           times={v_state.tradeRecord.length}
      />

      <Modal
        title={"历史数据回测"}
        visible={state.modalShow}
        onOk={ModalOnOk}
        onCancel={ModalOnCancel}
      >
        <div>

          <div style={{marginBottom: 10}}>
            <h3>股票代码</h3>
            <Input placeholder="股票代码" value={state.code} allowClear={true} onChange={InputCodeChange}/>
          </div>
          <div style={{marginBottom: 10}}>
            <h3>初始投资</h3>
            <Input placeholder="初始投资" value={state.invest} allowClear={true} onChange={InputInvestChange}/>
          </div>

          <Tabs defaultActiveKey={strategy} onChange={(value: string) => {
            console.log(value);
            setState({...state, strategy: value});
          }}>
            <TabPane tab="复合" key="complex">
              <div>
                <h2>买卖策略</h2>
                <Item title={"向上落差"}>
                  <Row>
                    <Col span={12}>
                      <Slider
                        min={0}
                        max={0.5}
                        onChange={value => {
                          setState({...state, up_threshold: Number(value)});
                        }}
                        value={typeof up_threshold === 'number' ? up_threshold : 0}
                        step={0.01}
                      />
                    </Col>
                    <Col span={4}>
                      <InputNumber
                        min={0}
                        max={1}
                        style={{marginLeft: 16}}
                        step={0.01}
                        value={up_threshold}
                        onChange={value => {
                          setState({...state, up_threshold: Number(value)});
                        }}
                      />
                    </Col>
                  </Row>
                </Item>

                <Item title={"向下落差"}>
                  <Row>
                    <Col span={12}>
                      <Slider
                        min={0}
                        max={0.5}
                        onChange={value => {
                          setState({...state, down_threshold: Number(value)});
                        }}
                        value={typeof down_threshold === 'number' ? down_threshold : 0}
                        step={0.01}
                      />
                    </Col>
                    <Col span={4}>
                      <InputNumber
                        min={0}
                        max={1}
                        style={{marginLeft: 16}}
                        step={0.01}
                        value={down_threshold}
                        onChange={value => {
                          setState({...state, down_threshold: Number(value)});
                        }}
                      />
                    </Col>
                  </Row>
                </Item>

                <h2>安全策略</h2>

                <Item title={"斩仓跌幅"}>
                  <Row>
                    <Col span={12}>
                      <Slider
                        min={0}
                        max={0.5}
                        onChange={value => {
                          setState({...state, safety_down: Number(value)});
                        }}
                        value={typeof safety_down === 'number' ? safety_down : 0}
                        step={0.01}
                      />
                    </Col>
                    <Col span={4}>
                      <InputNumber
                        min={0}
                        max={1}
                        style={{marginLeft: 16}}
                        step={0.05}
                        value={safety_down}
                        onChange={value => {
                          setState({...state, safety_down: Number(value)});
                        }}
                      />
                    </Col>
                  </Row>
                </Item>

                <Item title={"落安涨幅"}>
                  <Row>
                    <Col span={12}>
                      <Slider
                        min={0}
                        max={0.5}
                        onChange={value => {
                          setState({...state, safety_up: Number(value)});
                        }}
                        value={typeof safety_up === 'number' ? safety_up : 0}
                        step={0.01}
                      />
                    </Col>
                    <Col span={4}>
                      <InputNumber
                        min={0}
                        max={1}
                        style={{marginLeft: 16}}
                        step={0.05}
                        value={safety_up}
                        onChange={value => {
                          setState({...state, safety_up: Number(value)});
                        }}
                      />
                    </Col>
                  </Row>
                </Item>

                <Item title={"仓位策略"}>
                  <Row>

                    <Select defaultValue={initial_step} style={{width: 120}}
                            onChange={(value: string) => {
                              setState({...state, initial_step: value});
                            }}>
                      <Option value="sensitive">谨慎</Option>
                      <Option value="normal">一般</Option>
                      <Option value="bold">大胆</Option>
                    </Select>

                  </Row>
                </Item>

                <Item title={"冷静期(天)"}>
                  <Row>
                    <Col span={12}>
                      <Slider
                        min={0}
                        max={200}
                        onChange={value => {
                          setState({...state, cold_down_period: Number(value)});
                        }}
                        value={typeof cold_down_period === 'number' ? cold_down_period : 0}
                        step={5}
                      />
                    </Col>
                    <Col span={4}>
                      <InputNumber
                        min={0}
                        max={1000}
                        style={{marginLeft: 16}}
                        step={5}
                        value={cold_down_period}
                        onChange={value => {
                          setState({...state, cold_down_period: Number(value)});
                        }}
                      />
                    </Col>
                  </Row>
                </Item>
              </div>
            </TabPane>
            <TabPane tab="朴素" key="naive">

            </TabPane>
          </Tabs>


        </div>
      </Modal>

      <div>
        <Card style={{marginTop: 20}} title={"总览"}>
          <Basic data={v_state.data}/>
        </Card>

        <Card style={{marginTop: 20}} title={"收益"}>
          <Curved data={v_state.data}/>
        </Card>

        <Card style={{marginTop: 20}} title={"交易"}>
          <TradeTable data={v_state.tradeRecord}/>
        </Card>
      </div>
    </div>
  )
};

export default Stock;
