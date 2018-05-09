import { axiosInstance } from '../utils';


export const profileURL = 'api/v1/profile/';

export const putProfile = (phone_number, position, description, avatar) => {
        const data = {
                      phone_number,
                      position,
                      description,
                      avatar
                      };
        return axiosInstance.put(profileURL, data)
    }
