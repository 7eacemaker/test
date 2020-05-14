import React,{ useState } from "react";
import { Menu, Layout } from "antd";
import {
    DesktopOutlined,
    PieChartOutlined,
    FileOutlined,
    TeamOutlined,
    UserOutlined
} from "@ant-design/icons";

import './Aside.css';

const { Sider } = Layout;
const { SubMenu } = Menu;

function Aside() {
  const [collapsed, setCollapsed] = useState(false);

  const onCollapse = collapsed => {
    setCollapsed(collapsed);
  };

  return (
    <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
      <div className="logo" />
      <Menu theme="dark" defaultSelectedKeys={["1"]} mode="inline">
        <SubMenu key="sub1" icon={<UserOutlined />} title="Employees">
          <Menu.Item key="1">Prediction</Menu.Item>
          <Menu.Item key="2">Graphics</Menu.Item>
        </SubMenu>
        <SubMenu key="sub2" icon={<TeamOutlined />} title="RRHH">
          <Menu.Item key="3">Team</Menu.Item>
        </SubMenu>
      </Menu>
    </Sider>
  );
}

export default Aside;
