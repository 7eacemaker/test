import React, { Fragment, useEffect, useState } from "react";
import { Form, Button, Upload, Table } from "antd";
import { UploadOutlined } from "@ant-design/icons";
import './EmployeesPrediction.css';

import { uploadExcelFile } from "../../services/employeeService";

function EmployeesPrediction() {
  const columns = [
    {
      title: "FullName",
      dataIndex: "TRABAJADOR"
    },
    {
      title: "Genre",
      dataIndex: "SEXO"
    },
    {
      title: "Document",
      dataIndex: "NRO_DOC_IDENTIDAD"
    },
    {
      title: "Prediction",
      dataIndex: "predictionText"
    },
     {
      title: "Probabilidad",
      dataIndex: "probabilidad"
    }
  ];

  const [data, setData] = useState([]);
  const [fileList, setFileList] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [loadingTable,setLoadingTable] = useState(false);

  const handleUpload = async () => {
    setData([]);
    setUploading(true);
    setLoadingTable(true);
    const formData = new FormData();
    formData.append("file", fileList[0]);

    let response = await uploadExcelFile(formData);
    setUploading(false);
    setLoadingTable(false);
    setData(response.data.prediction);
  };

  const props = {
    onRemove: file => {
      const index = fileList.indexOf(file);
      const newFileList = fileList.slice();
      newFileList.splice(index, 1);
      setFileList(newFileList);
      return {
        fileList: newFileList
      };
    },
    beforeUpload: file => {
      setFileList([...fileList, file]);
      return false;
    },
    fileList
  };

  return (
    <Fragment>
      <div className="uploadContainer">
        <Upload {...props}>
          <Button>
            <UploadOutlined /> Select File
          </Button>
        </Upload>
        <Button
          type="primary"
          onClick={handleUpload}
          disabled={fileList.length === 0}
          loading={uploading}
          style={{}}
        >
          {uploading ? "Uploading" : "Start Upload"}
        </Button>
      </div>

      <Table dataSource={data} columns={columns} className="dataTable" loading={loadingTable}/>
    </Fragment>
  );
}

export default EmployeesPrediction;
