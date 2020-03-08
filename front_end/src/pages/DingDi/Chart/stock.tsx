import React, {useState} from "react";
import {Button, Modal, Input, Switch} from "antd";
import Basic from "./multipleChart";

import service from "../Service"

interface StockProps {

}

// interface StockState {
//   data: any
// }

let data = require("./result.json");

const Stock: React.FC<StockProps> = props => {

  const [state, setState] = useState({
    data: data as any,
    modalShow: false,
    code: "000596" as string,
    combineDingDi: true,
    adjustment:false,
    regressModal:false
  });

  // ding di
  const InputCodeChange = (event: any) => {
    setState({...state, code: event.target.value})
  };

  const gainDingDi = async () => {
    const data = await service.queryDingDi(state.code, state.combineDingDi, state.adjustment);
    setState({...state, modalShow: false, data: data});
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

  return (
    <div>
      <Button type="primary" onClick={ButtonOnClick}>
        顶底识别
      </Button>

      <Modal
        title={"顶底识别"}
        visible={state.modalShow}
        onOk={ModalOnOk}
        onCancel={ModalOnCancel}
      >
        <div>
          <div>
            <p>股票代码</p>
            <Input placeholder="股票代码" allowClear={true} onChange={InputCodeChange}/>
          </div>
          <div style={{marginTop: 15}}>
            <label style={{marginRight: 15}}>合并顶底</label>
            <Switch defaultChecked={state.combineDingDi} onChange={value => {
              setState({...state, combineDingDi: value});
            }}/>
          </div>
          <div style={{marginTop: 15}}>
            <label style={{marginRight: 15}}>滞后纠正</label>
            <Switch defaultChecked={state.adjustment} onChange={value => {
              setState({...state, adjustment: value});
            }}/>
          </div>
        </div>
      </Modal>

      <div style={{marginTop:20}}>
        <h3>股票代码:{state.code}</h3>
      </div>

      <div style={{marginTop:20}}>
        <Basic data={state.data}/>
      </div>
    </div>
  )
};

export default Stock;
