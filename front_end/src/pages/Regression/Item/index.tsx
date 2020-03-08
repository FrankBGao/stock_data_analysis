import React from 'react';
import style from './index.less';

export interface ItemProps {
    /** 自定义样式  */
    style?: React.CSSProperties;
    /** 标题 */
    title: string;
    /** 内容区域 */
    children: React.ReactNode; // any | JSX.Element[]
}

const Item: React.FC<ItemProps> = ({ title, children }) => {
    return (
        <div className={style["itemP"]}>
            <div className={style["itemP-title"]}>{title}</div>
            <div className={style["itemP-children"]}>{children}</div>
        </div>
    );
};

export default Item;
