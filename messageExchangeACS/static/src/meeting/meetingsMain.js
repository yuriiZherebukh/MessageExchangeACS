import React from "react";

import HomeNavigation from "../home/home_navigation";
import '../home/home.less';
import Meetings from "./meetings";

export default class MeetingsMain extends React.Component {

    render() {
        return (
          <div className='HolyGrail'>
                <div className='homePage'>
                   <div className='homeContent'>
                      <Meetings />
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
