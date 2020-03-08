import request from '@/utils/request';

import {message} from "antd";

const checkLogout = (data: any) => {
  if (data.logout != undefined) {
    message.warning("已被登出，请重新登陆");
  }
};

const queryRegression = async (code:string,option:any,) => {
  const data = await request('/server/api/regress', {
    method: 'POST',
    data: {
      code: code,
      option:option,
    },
  });
  checkLogout(data);
  // console.log(data);
  // console.log(typeof data);

  return new Promise(resolve =>
    resolve(data),
  )
};


//refresh file
const queryRefresh = async () => {
  const data = await request.get('/server/api/refresh_code_data', {
  });
  //{"col": ["aa", "bb"]}
  checkLogout(data);
  return new Promise(resolve =>
    resolve(data),
  );
};


//upload file col setting
// const sendDataColNameSetting = async (setting:any, userID?:string) => {
//   const data = await request.get('/server/api/file_col_setting', {
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
//   const data = await request('/server/api/indicator_dashboard/save', {
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
  queryRegression,
  queryRefresh
};







// if(typeof data === "string"){
//   return new Promise(resolve =>
//     resolve(JSON.parse(data)),
//   )
// }else {
//   return new Promise(resolve =>
//     resolve(data),
//   )
// }
