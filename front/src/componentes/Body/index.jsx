import axios from 'axios';
import * as FileIconsBs from 'react-icons/bs'
import * as FileIconsTi from 'react-icons/ti'
import React, { Component} from 'react';
import '../../componentes/Body/styles.css'
import Header from '../Header'
// import { render } from '@testing-library/react';
// import Relatorio from '../relatorio';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';



class Body extends Component {

 

  axiosConfig = {headers: {

    "Access-Control-Allow-Origin": "*"
}}

constructor () {
  super();
  this.state = {
    selectedFile: null,
    file2: null
  };
  this.handleChange = this.handleChange.bind(this);
}


  /* state = {selectedFile:null,
             file2:null
            } */

 

  // On file select (from the pop up)
  handleChange(event, indice) {
    
    // Update the state
    this.setState({[indice] : event.target.files[0]});
    console.log(this.state.selectedFile)
    
  };
 

  // On file upload (click the upload button)
  onFileUpload = () => {

      toast.info('Please, active the website pop-ups and redirection!', {
      position: "top-left",
      autoClose: 9000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });

    console.log(this.state.selectedFile)
    console.log(this.state.file2)
    console.log("chamou o onFileUpload")
    document.getElementById("div-btn-generate").style.display = "none";
    document.getElementById("upload").style.display = "none";
    document.getElementById("loading").style.display = "block"
    
    if(this.state.selectedFile&&this.state.file2){
      console.log("state e state2 true")
        // Create an object of formDatas
        const formData = new FormData();
        const formData2 = new FormData();

        // Update the formData object
        formData.append(
          "inputFile",
          this.state.selectedFile,
          this.state.selectedFile.name
        );
        
        formData2.append(
          "inputFilePeriferico",
          this.state.file2,
          this.state.file2.name
        );

        // Details of the uploaded file
        console.log(this.state.selectedFile);
        console.log(this.state.file2);

        // Request made to the backend api
        // Send formData object
        axios.post("http://150.165.167.59:5000/upload", formData, this.axiosConfig).then(function (response) {
          console.log(response)
          document.getElementById("loading").style.display = "none"
          document.getElementById("finish").style.display = "block"

        }).catch(function (error) {
          console.log(error.toJSON());
          document.getElementById("div-btn-generate").style.display = "flex";
          document.getElementById("upload").style.display = "flex";
          document.getElementById("loading").style.display = "none";
          toast.error('Error, please try later.', {
            position: "top-left",
            autoClose: 9000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
          });

        });

        axios.post("http://150.165.167.59:5000/upload-perifericos", formData2, this.axiosConfig).then(function (response) {

          console.log(response.data)
         
        }).catch(function (error) {
          console.log(error.toJSON());
          document.getElementById("div-btn-generate").style.display = "flex";
          document.getElementById("upload").style.display = "flex";
          document.getElementById("loading").style.display = "none";
          toast.error('Error, please try later.', {
            position: "top-left",
            autoClose: 9000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
          });

        });
        
    }
      if(this.state.selectedFile&&!this.state.file2){
        console.log("state true")
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
        axios.post("http://150.165.167.59:5000/upload", formData, this.axiosConfig ).then(function (response) {
          
          document.getElementById("loading").style.display = "none"
          document.getElementById("finish").style.display = "block"
          console.log(response) 
          

        }).catch(function (error) {
          console.log(error.toJSON());
          document.getElementById("div-btn-generate").style.display = "flex";
          document.getElementById("upload").style.display = "flex";
          document.getElementById("loading").style.display = "none"
          toast.error('Error, please try later.', {
            position: "top-left",
            autoClose: 9000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
          });
          
           
        });
        

      }
      /* if(!this.state.selectedFile&&this.state.file2){
        console.log("state2 true")
        // Create an object of formDatas
       
        const formData2 = new FormData();

        // Update the formData object
        
        
        formData2.append(
          "inputFilePeriferico",
          this.state.file2,
          this.state.file2.name
        );

        // Details of the uploaded file
        
        console.log(this.state.file2);

        // Request made to the backend api
        // Send formData object
        
        axios.post("http://150.165.167.59:5000/upload-perifericos", formData2, this.axiosConfig).then(function (response) {
          document.getElementById("loading").style.display = "none"
          document.getElementById("finish").style.display = "block"
          console.log(response)
          window.open('/relatorio')
        }).catch(function (error) {
          document.getElementById("div-btn-generate").style.display = "flex";
          document.getElementById("upload").style.display = "flex";
          document.getElementById("loading").style.display = "none"
          toast.error('Error, please try later.', {
            position: "top-left",
            autoClose: 9000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
          });
          
          

        });
 
      }
*/
  };

  
  restart = () => {

    document.getElementById("div-btn-generate").style.display = "flex";
    document.getElementById("finish").style.display = "none"
    document.getElementById("upload").style.display = "flex";
    window.open('/relatorio')
  }

  // File content to be displayed after
  // file upload is complete

  render() {


    return (
      <div style={{ display: 'block' }}>
        <Header />
        <div id="body">
        <ToastContainer
              position="top-right"
              autoClose={5000}
              hideProgressBar={false}
              newestOnTop={false}
              closeOnClick
              rtl={false}
              pauseOnFocusLoss
              draggable
              pauseOnHover
              />
{/* Same as */}
<ToastContainer />


          <div className="localContainer">
            <div>
              <h3 className='title'>CREATE LOCAL REPORT</h3>
            </div>
            <div className="stepsIcons">
              <div className="fileIcon">
                <i className="itemFile">
                  <FileIconsBs.BsFileEarmarkCode size={35} color="#001866" style={{ padding: 6 }} />
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
                Click in the circle below and choose a <strong className="strongLog">Log.csv </strong>
                and <strong className="strongLog">Peripheral.csv </strong>file from your device.
              </h4>
            </div>
           <div id="upload" className="upload">
           <div id="uploadSpace" className="uploadSpace">
              <input id="fileUp" type="file" name="upload_file" accept=".csv" onChange={(event)=>this.handleChange(event, "selectedFile")} />
              <label htmlFor="fileUp">
                <button className="uploadIcon">
                  <FileIconsTi.TiUpload color="white" size={70} />
                </button>
              </label>

              <h4 className="textDownUpload">Choose a Log.csv file</h4>
            </div>

            <div id="uploadSpace" className="uploadSpace">
              <input id="fileUp2" type="file" name="upload_file_periferico" accept=".csv, .xlsx" onChange={(event)=>this.handleChange(event, "file2")} />
              <label htmlFor="fileUp2">
                <button className="uploadIcon">
                  <FileIconsTi.TiUpload color="white" size={70} />
                </button>
              </label>
              <h4 className="textDownUpload">Choose a Peripheral.csv file</h4>
            </div>
          </div> 
            

            <div id="div-btn-generate">
              <button id='button' className="buttonGenerate"  disabled={this.state.selectedFile==null} onClick={this.onFileUpload}>Generate</button>
            </div>

            <div id="finish" className="finish" style={{ display: "none" }}>
              <h2 style={{ textAlign: 'center', marginTop: 10, color: '#373A3C', fontFamily: 'Mulish' }}>Success</h2>
              <h4 style={{ textAlign: 'center', marginTop: 10, color: '#373A3C', fontFamily: 'Mulish' }}>The Health Check Report was successfully generated!</h4>
              <button id="bnt-ok" className="bnt-ok" onClick={this.restart}>OK</button></div>

            <div id="loading" className="loading" style={{ display: "none" }}>
              <div className="lds-dual-ring"></div>
              <h3 style={{ textAlign: 'center', marginTop: 40, color: '#373A3C', fontFamily: 'Mulish' }}>Generating Health Check Report</h3>
              <h4 style={{ textAlign: 'center', marginTop: 20, color: '#373A3C', fontFamily: 'Mulish' }}>Please wait...</h4></div>
             <div id="erro" style={{display:'none'}}>
                <h3 className="erro">Something went wrong, please try again later</h3>
                <button id="bnt-ok" className="bnt-ok" onClick={this.restart}>OK</button>
             </div>
              

            <div className="space"></div>

          </div>

        </div>

      </div>

    );
  }
}

export default Body;