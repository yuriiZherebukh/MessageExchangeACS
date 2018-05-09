import React from "react";

import Paper from "material-ui/Paper";

import MessageButtons from "./message_buttons";
import HomeNavigation from "../home/home_navigation";
import '../home/home.less';
import "./message.less";


export default class Message extends React.Component{

    render(){
        return(
          <div className='HolyGrail'>
                <div className='homePage'>
                   <div className='homeContent'>
                     <div className='helpPage'>

                         <Paper className="helpPaper" zDepth={1}>
                            <MessageButtons handler={this.props.handler}/>
                         </Paper>

                         <div className='side'>
                         </div>
                     </div>
                   </div>
                   <div className='homeNavigation'>
                       <HomeNavigation />
                   </div>
                   <aside className='HolyGrail-right'>
                   </aside>
               </div>
           </div>



       )
   }
}
