import React from "react";
import { Layout, Breadcrumb } from "antd";
import './Home.css';

import Aside from '../../components/aside/Aside';
import HeaderOwn from '../../components/header/Header';
import EmployeesPrediction from '../../components/employees/EmployeesPrediction';

const { Content, Footer } = Layout;

function Home() {
  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Aside />

      <Layout className="site-layout">
        <HeaderOwn />

        <Content style={{ margin: "0 16px" }}>
          <Breadcrumb style={{ margin: "16px 0" }}>
            <Breadcrumb.Item>Employees</Breadcrumb.Item>
            <Breadcrumb.Item>Prediction</Breadcrumb.Item>
          </Breadcrumb>

          
          <div
            className="site-layout-background"
            style={{ padding: 24, minHeight: 360 }}
          >
              <EmployeesPrediction />
          </div>


        </Content>

        <Footer style={{ textAlign: "center" }}>Light White @2020</Footer>
      </Layout>
    </Layout>
  );
}

export default Home;
