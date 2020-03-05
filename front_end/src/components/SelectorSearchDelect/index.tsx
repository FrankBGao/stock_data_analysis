import { Select} from 'antd';
import React, {Component} from 'react';

interface SelectorProps {
  Options:string[],
  onChange:any,
  onClick:any,
  selectItem?:string[]
}

class SelectWithHiddenSelectedOptions extends Component<SelectorProps> {
  constructor(props:{Options:string[], onChange:any, selectItem?:string[]}){//
    super(props);

    let inter:string[];
    if(props.selectItem){
      inter = props.selectItem
    }else {
      inter =[]
    }

    this.state = {
      selectedItems: inter ,
    };
  }

  handleChange = selectedItems => {
    this.setState({ selectedItems:selectedItems });
    this.props.onChange(selectedItems);//frank. 对外的function
  };

  handleClick = () => {
    this.props.onClick();//frank. 对外的function
  };


  render() {
    const { selectedItems } = this.state;
    const OPTIONS = this.props.Options;
    const filteredOptions = OPTIONS.filter(o => !selectedItems.includes(o));
    return (
      <Select
        mode="multiple"
        placeholder="输入联想"
        value={selectedItems}
        onChange={this.handleChange}
        onFocus={this.handleClick}
        style={{ width: '100%' }}
      >
        {filteredOptions.map(item => (
          <Select.Option key={item} value={item}>
            {item}
          </Select.Option>
        ))}
      </Select>
    );
  }
}
export default SelectWithHiddenSelectedOptions;
