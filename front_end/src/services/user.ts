import request from '@/utils/request';

export async function query(): Promise<any> {
  return request('/api/users');
}

export async function queryCurrent(): Promise<any> {
  return request('/stock/api/currentUser');//#frank, login in page, first here
}

export async function queryNotices(): Promise<any> {
  return request('/api/notices');
}

//findprocess
export async function queryLogout(): Promise<any> {
  return request('/stock/api/logout');
}

export async function queryCheckUserServerState(userid:string): Promise<any> {
  return request('/stock/api/currentUserState',
    {
      data: {userid:userid},
    }

  );
}
