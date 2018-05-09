import { axiosInstance } from '../utils';

const classroomUrl = '/api/v1/classroom/';

export const postClassroom = (number, size) => {
    return axiosInstance.post(classroomUrl, {
        number,
        size
    })
};

export const getClassroom = (classroom_id) => {
    return axiosInstance.get(classroomUrl + classroom_id + '/')

};

export const getClassrooms = () => {
    return axiosInstance.get(classroomUrl)

};
