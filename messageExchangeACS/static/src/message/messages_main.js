import React from "react";

import HomeNavigation from "../home/home_navigation";
import '../home/home.less';
import Messages from "./messages";

export default class MessagesMain extends React.Component {

    render() {
        return (
          <div className='HolyGrail'>
                <div className='homePage'>
                   <div className='homeContent'>
                      <Messages />
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
