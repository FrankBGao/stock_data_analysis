import React, {useState} from "react";
// import {Card} from "antd";
import ReactEcharts from "echarts-for-react";
import heatMap from "./picData"
import {Button, Col, Input, message, Modal, Select, Switch} from "antd";
import service from "../Service"

const tree = require("./data.json");
const indusList = require("./indus.json");

const {Option} = Select;
const Chart: React.FC<{}> = props => {

  const [state, setState] = useState({
    modalShow: false,

    refreshLabel: "未更新" as string,
    tree: tree,
    treeName: "示例",
    indus: "none" as string,
    allMarket: true as boolean,
    indusList:indusList.slice(0,5) as string[]
  });

  const {indus, allMarket} = state;

  const ButtonOnClick = () => {
    setState({...state, modalShow: true});
  };

  const gainHeatmap = async ()=>{
    message.loading({content:"计算中", key: "calculating", duration:1000});
    const data = await service.queryHeatmap(state.allMarket, state.indus);
    if(data===false){
      message.warning({content:"计算失败", key: "calculating"});
      return
    }
    setState({...state, tree:JSON.parse(data), modalShow: false, treeName:allMarket?"全市场":indus});
    message.success({content:"计算完成", key: "calculating"});
  };

  const ModalOnOk = () => {
    gainHeatmap().then();

  };

  const ModalOnCancel = () => {
    setState({...state, modalShow: false});
  };

  const RefreshData = async ()=>{
    message.loading({content:"下载中", key: "refreshing", duration:1000});
    const data = await service.queryRefreshing();
    if(data===false){
      message.warning({content:"下载失败", key: "refreshing"});
      setState({...state, refreshLabel: "下载失败"});
      return
    }
    setState({...state, refreshLabel: "下载成功"});
    message.loading({content:"下载完成", key: "refreshing"});
  };

  const ButtonRefreshOnClick = () => {
    RefreshData().then();
  };

  const onSearch = (val:any)=> {
    let result = [];
    setState({...state, indusList: []});
    for(const i of indusList){
      if(i.indexOf(val)!=-1){
        result.push(i)
      }

      if(result.length > 4){
        setState({...state, indusList: result});
        return
      }
    }
    setState({...state, indusList: result});
  };


  return (
    <div>
      <Button onClick={ButtonOnClick} type="danger">
        更新图形
      </Button>

      <Button onClick={ButtonRefreshOnClick} style={{marginLeft: 15}} type="danger">
        更新数据
      </Button>

      <label style={{marginLeft: 15}}>
        {state.refreshLabel}
      </label>

      <Modal
        title={"更新图形"}
        visible={state.modalShow}
        onOk={ModalOnOk}
        onCancel={ModalOnCancel}
      >
        <div>

          <div style={{marginBottom: 10}}>
            <h3>全市场</h3>
            <Switch defaultChecked={allMarket} onChange={(value: boolean) => {
              setState({...state, allMarket: value});
            }}/>
          </div>

          <div style={{marginBottom: 10}}>
            <h3>行业</h3>
            <Select
              showSearch
              disabled = {state.allMarket}
              style={{width: 200}}
              placeholder="行业"
              optionFilterProp="children"
              onChange={(value: string) => {
                console.log("hi");
                setState({...state, indus: value});
              }}
              onSearch={onSearch}
              onFocus={() => {
              }}

            >
              {state.indusList.map((obj: string) => {
                return <Option value={obj}>{obj}</Option>
              })}
            </Select>
          </div>


        </div>
      </Modal>

      <ReactEcharts
        option={heatMap(state.tree, state.treeName)}
        style={{
          height: window.innerHeight > 1000 ? 800 : window.innerHeight - 50,
          width: '100%'
        }}
      />
    </div>
  )
};

export default Chart;
