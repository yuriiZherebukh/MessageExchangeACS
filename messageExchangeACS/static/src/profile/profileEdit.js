import React from "react";
import Dropzone from 'react-dropzone';
import axios from 'axios';
import moment from 'moment';
import { onlyAlpha, onlyDigit } from './../utils';
import { putProfile, profileURL } from './profile.service';

import FlatButton from 'material-ui/FlatButton'
import TextField from 'material-ui/TextField';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import Snackbar from 'material-ui/Snackbar';
import AvatarIcon from 'material-ui/svg-icons/image/portrait';
import SaveIcon from 'material-ui/svg-icons/navigation/check';
import DatePicker from 'material-ui/DatePicker';
import { blue500 } from 'material-ui/styles/colors';

import './profile.less';

const styles = {
  LabelStyle: {
    color: blue500,
  },
  buttonStyle: {
    margin: 18,
  },
};

export class ProfileEdit extends React.Component {
    constructor(props){
        super(props);
        this.state = props.profile;
        this.state.open = false;
    };

    handleChangePhoneNumber = (event) => this.setState({phone_number: event.target.value});

    handleChangeDescription = (event) => this.setState({description: event.target.value});

    handleChangePosition = (event, index, value) => this.setState({position: value});

    profileEdit = () => {
    const user = this.state.user;
        const phone_number = this.state.phone_number;
        const position = this.state.position;
        const description = this.state.description;
        putProfile(phone_number, position, description)
        .then(this.props.getProfile());
    }

    render()
       {
        return(
      <div className='textBlock'>
            <TextField
            floatingLabelText="Email:"
            name="Email"
            value={this.state.user.email}
            fullWidth={true}
            underlineShow={false}
            floatingLabelStyle={styles.LabelStyle}
            />
        <TextField
          floatingLabelText="Name:"
          name="first_name"
          value={this.state.user.first_name}
          fullWidth={true}
          floatingLabelStyle={styles.LabelStyle}
        />

        <TextField
          floatingLabelText="Surname:"
          name="last_name"
          value={this.state.user.last_name}
          fullWidth={true}
          floatingLabelStyle={styles.LabelStyle}
        />

        <TextField
          floatingLabelText="Phone number:"
          name="phone_number"
          value={this.state.phone_number}
          fullWidth={true}
          onChange={this.handleChangePhoneNumber}
          floatingLabelStyle={styles.LabelStyle}
        />

        <SelectField
          floatingLabelText="Position:"
          name='position'
          value={this.state.position}
          onChange={this.handleChangePosition}
          autoWidth={true}
          floatingLabelStyle={styles.LabelStyle}>
          <MenuItem key={1} value={'AS'} primaryText="Assistant" />
          <MenuItem key={2} value={'EN'} primaryText="Engineer" />
          <MenuItem key={3} value={'DC'} primaryText="Docent" />
          <MenuItem key={4} value={'PS'} primaryText="Professor" />
          <MenuItem key={5} value={'LA'} primaryText="laboratorian worker" />
          <MenuItem key={6} value={'AD'} primaryText="Administrator" />
          <MenuItem key={7} value={'SC'} primaryText="Secretary" />
          <MenuItem key={8} value={'AC'} primaryText="Accountant" />
          <MenuItem key={9} value={'PR'} primaryText="Pro-rector" />
          <MenuItem key={10} value={'DP'} primaryText="Head of Department" />
          <MenuItem key={11} value={'RC'} primaryText="Rector" />
          <MenuItem key={12} value={'DR'} primaryText="Director" />
        </SelectField>

        <TextField
          floatingLabelText="Description:"
          name='description'
          value={this.state.description}
          fullWidth={true}
          multiLine={true}
          rowsMax={10}
          onChange={this.handleChangeDescription}
          floatingLabelStyle={styles.LabelStyle}
        />
        <FlatButton onTouchTap={this.profileEdit}
        label="Save changes " labelPosition="before" icon={<SaveIcon /> }
        primary={true} fullWidth={true} rippleColor={blue500} />

      </div>
    );
};
}