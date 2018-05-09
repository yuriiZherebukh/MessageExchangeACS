import { axiosInstance } from '../utils';

const meetingUrl = '/api/v1/meeting/';

export const postMeeting = (classroom, participated_user, name, description, date_of_action, starts_at, finishes_at) => {
    return axiosInstance.post(meetingUrl, {
        classroom,
        participated_user,
        name,
        description,
        date_of_action,
        starts_at,
        finishes_at
    })
};

export const getMeeting = (meeting_id) => {
    return axiosInstance.get(meetingUrl + meeting_id + '/')

};

export const getMeetings = () => {
    return axiosInstance.get(meetingUrl)

};
