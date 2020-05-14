import axiosClient from '../config/axios';

export const uploadExcelFile = async (data) => {
    return await axiosClient.post('/employee',data);
}