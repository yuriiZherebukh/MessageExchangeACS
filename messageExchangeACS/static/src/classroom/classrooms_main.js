import React from "react";

import HomeNavigation from "../home/home_navigation";
import '../home/home.less';
import Classrooms from "./classrooms";

export default class ClassroomsMain extends React.Component {

    render() {
        return (
          <div className='HolyGrail'>
                <div className='homePage'>
                   <div className='homeContent'>
                      <Classrooms />
                   </div>
                   <div className='homeNavigation'>
                       <HomeNavigation />
                   </div>
                   <aside className='HolyGrail-right'>
                   </aside>
               </div>
           </div>
        );
    }
}
