import { axiosInstance } from '../utils';

const messageUrl = '/api/v1/message/';
const usersURL = '/api/v1/auth/user/';

export const postMessage = (header, body, to_users) => {
    return axiosInstance.post(messageUrl, {
        header,
        body,
        to_users
    })
};

export const getMessage = (message_id) => {
    return axiosInstance.get(messageUrl + message_id + '/')

}

export const getMessages = (message_id) => {
    return axiosInstance.get(messageUrl)

}

export const getSentMessages = (message_id) => {
    return axiosInstance.get(messageUrl + 'sent/')

}


export const getUsers = () =>{
    return axiosInstance.get(usersURL)
}

