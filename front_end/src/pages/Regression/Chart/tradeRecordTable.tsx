import React from "react";
import {Table, Tag} from "antd";

interface TableProps {
  data: any
}

const TradeTable: React.FC<TableProps> = props => {
  const columns = [
    {
      title: '日期',
      dataIndex: 'date',
      key: 'date',
    },
    {
      title: '收益率',
      dataIndex: 'earn_percentage',
      key: 'earn_percentage',
    },
    {
      title: '价格',
      dataIndex: 'price',
      key: 'price',
    },
    {
      title: '量(手)',
      dataIndex: 'quantity',
      key: 'quantity',
    },
    // {
    //   title: '',
    //   dataIndex: 'amount',
    //   key: 'amount',
    // },
    {
      title: '交易类型',
      key: 'type_is',
      dataIndex: 'type_is',
      render: tags => (
        <span>
            <Tag color={tags==="buy"?'volcano':'green'} key={tags}>
              {tags}
            </Tag>
      </span>
      ),
    },
    {
      title: '交易细节',
      dataIndex: 'option',
      key: 'option',
    },
    // {
    //   title: '总值',
    //   dataIndex: 'all_money',
    //   key: 'all_money',
    // },

  ];

  // const data = [
  //   {
  //     key: '1',
  //     name: 'John Brown',
  //     age: 32,
  //     address: 'New York No. 1 Lake Park',
  //     tags: ['nice', 'developer'],
  //   },
  //   {
  //     key: '2',
  //     name: 'Jim Green',
  //     age: 42,
  //     address: 'London No. 1 Lake Park',
  //     tags: ['loser'],
  //   },
  //   {
  //     key: '3',
  //     name: 'Joe Black',
  //     age: 32,
  //     address: 'Sidney No. 1 Lake Park',
  //     tags: ['cool', 'teacher'],
  //   },
  // ];


  return (
    <div>
      <Table columns={columns} dataSource={props.data}/>
    </div>
  )
};

export default TradeTable;
