import request from '@/utils/request';

import {message} from "antd";

const checkLogout = (data: any) => {
  if (data.logout != undefined) {
    message.warning("已被登出，请重新登陆");
  }
};

//upload file
const queryDingDi = async (code:string, combineDingDi:boolean, adjustment:boolean) => {
  const data = await request.get('/stock/api/ding_di', {
    params: {
      code: code,
      combineDingDi: combineDingDi,
      adjustment: adjustment,
    }
  });
  //{"col": ["aa", "bb"]}
  checkLogout(data);
  console.log(data);
  return new Promise(resolve =>
    resolve(data),
  );
};

//refresh file
const queryRefresh = async (code:string) => {
  const data = await request.get('/stock/api/refresh_code_data', {
    params: {
      code: code,
    }
  });
  //{"col": ["aa", "bb"]}
  checkLogout(data);
  return new Promise(resolve =>
    resolve(data),
  );
};

//upload file col setting
// const sendDataColNameSetting = async (setting:any, userID?:string) => {
//   const data = await request.get('/stock/api/file_col_setting', {
//     params: {
//       userID: "this",
//       setting: setting
//     }
//   });
//   //{"result": "success"}
//   checkLogout(data);
//   return new Promise(resolve =>
//     resolve(data),
//   );
// };


///////////////////////////////////////
// dashboard
//////////////////////////////////////

//Save Dashboard
// const querySaveDashboard = async (dashBoardID:string,dashBoardName:string,description:string,dashBoardElement:any,) => {
//   const data = await request('/stock/api/indicator_dashboard/save', {
//     method: 'POST',
//     data: {
//       dashBoardID: dashBoardID,
//       dashBoardName:dashBoardName,
//       description:description,
//       dashBoardElement: dashBoardElement
//     },
//   });
//   //{"col": ["aa", "bb"]}
//   checkLogout(data);
//   return new Promise(resolve =>
//     resolve(data),
//   );
// };


export default {
  queryDingDi,
  queryRefresh
};
