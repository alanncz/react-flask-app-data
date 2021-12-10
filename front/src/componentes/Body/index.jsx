import axios from 'axios';
import * as FileIconsBs from 'react-icons/bs'
import * as FileIconsTi from 'react-icons/ti'
import React,{Component, useState} from 'react';
import '../../componentes/Body/styles.css'
import Header from '../../componentes/Header'
import { render } from '@testing-library/react';
import Relatorio from '../relatorio';

// import Relatorio from '../relatorio';
// import { render } from '@testing-library/react';

 
class Body extends Component {
   
    state = {
      // Initially, no file is selected
      selectedFile: null
    };
    
    // On file select (from the pop up)
    onFileChange = event => {
    
      // Update the state
      this.setState({ selectedFile: event.target.files[0] });
    
    };
    
    // On file upload (click the upload button)
    onFileUpload = () => {
        
        document.getElementById("div-btn-generate").style.display = "none";
        document.getElementById("uploadSpace").style.display = "none";
        
     

      document.getElementById("loading").style.display = "block"
      
      // Create an object of formDatas
      const formData = new FormData();
    
      // Update the formData object
      formData.append(
        "inputFile",
        this.state.selectedFile,
        this.state.selectedFile.name
      );
    
      // Details of the uploaded file
      console.log(this.state.selectedFile);
    
      // Request made to the backend api
      // Send formData object
	  //axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
	  //axios.defaults.headers.post['Access-Control-Allow-Headers'] = 'Content-Type';
      axios.post("http://localhost:5000/upload", formData).then(function (response){
        document.getElementById("loading").style.display = "none"
        document.getElementById("finish").style.display = "block"
        window.open('/relatorio')
      });
      
      
        
    };
    restart=()=> {
      
        document.getElementById("div-btn-generate").style.display = "flex";
        document.getElementById("finish").style.display = "none"
        document.getElementById("uploadSpace").style.display = "block";
    }
    
    // File content to be displayed after
    // file upload is complete
   
    render() {
      
      return (
        <div style={{display:'block'}}>
          <Header/>
        <div id="body">
          
            <div className="localContainer">
                    <div>
                        <h3 className='title'>CREATE LOCAL REPORT</h3>
                    </div>
                    <div className="stepsIcons">
                        <div className="fileIcon">
                                <i class="itemFile">
                                <FileIconsBs.BsFileEarmarkCode size={35} color="#001866" style={{padding: 6}}/>
                                </i>
                            <div className="arrowDown"></div>
                            
                        </div>                        
                    </div>
                    <div>
                        <h3 className="title2">
                            Upload Log File
                        </h3>
                    </div>
                    <div>
                        <h4 className="textUpload">
                            Click in the circle below and choose a <strong className="strongLog">Log.xlsx </strong> 
                            file from your device.
                        </h4>
                    </div>
                    <div id="uploadSpace" className="uploadSpace">
                    <input id="fileUp" type="file" name="upload_file" onChange={this.onFileChange} />
                    <label htmlFor="fileUp">
                    <button className="uploadIcon">
                        <FileIconsTi.TiUpload color="white" size={70} />
                    </button>
                    </label>
                      
                    <h4 className="textDownUpload">Choose a file</h4>
                    
                    </div>
                    <div id="div-btn-generate">
                    <button id="buttonGenerate" className="buttonGenerate" id='button' disabled={!this.state.selectedFile} onClick={this.onFileUpload}>Generate</button>
                    </div>
                   
                    <div id="finish" class="finish" style={{display:"none"}}>
                      <h2 style={{textAlign:'center', marginTop:10, color:'#373A3C', fontFamily:'Mulish'}}>Success</h2>
                    <h4 style={{textAlign:'center', marginTop:10, color:'#373A3C', fontFamily:'Mulish'}}>The Health Check Report was successfully generated!</h4>
                    <button id="bnt-ok" class="bnt-ok" onClick={this.restart}>OK</button></div>
                    
                    <div id="loading" class="loading" style={{display:"none"}}>
                    <div class="lds-dual-ring"></div>
                      <h3 style={{textAlign:'center', marginTop:40, color:'#373A3C', fontFamily:'Mulish'}}>Generating Health Check Report</h3>
                      <h4 style={{textAlign:'center', marginTop:20,color:'#373A3C',fontFamily:'Mulish'}}>Please wait...</h4></div>
                    <div className="space"></div>

            </div>
            
        </div>
        
        </div>
       
      );
    }
  }
 
  export default Body;