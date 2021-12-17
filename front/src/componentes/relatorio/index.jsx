
import '../relatorio/styles.css'
import logoAi from '../../imagens/logoAi.png'
import logo2 from '../../imagens/pngegg.png'
import background_image from '../../imagens/background-TRANSP.png'
import Plot from 'react-plotly.js'
import { useEffect, useState } from 'react'
import axios from 'axios'


function Relatorio() {

    const [figura330, setFigura330] = useState([])
    

    const [figura250, setFigura250] = useState([])
    

    const [figura390, setFigura390] = useState([])
   

    const [reset, setReset] = useState([])
    const [load_capacity, setLoadCapacity] = useState([])
    const [motorSpd, setMotorSpd] = useState([])
    const [speed_limits, setSpeed_limits] = useState([])
    const [fence_open, setFence_open] = useState([])
    

   /*  const [figura205, setFigura205] = useState([])
    const [figura220, setFigura220] = useState([])
    const [figura240, setFigura240] = useState([])
    
    const [figura255, setFigura255] = useState([])
    
    const [figura400, setFigura400] = useState([])
    const [figura420, setFigura420] = useState([])
    const [figura440, setFigura440] = useState([])
    const [figura450, setFigura450] = useState([])
    const [figura470, setFigura470] = useState([])
    const [figura480, setFigura480] = useState([])
    const [figura550, setFigura550] = useState([])
    const [figura560, setFigura560] = useState([])
    const [figura570, setFigura570] = useState([])
    const [figura580, setFigura580] = useState([])  */


    const [valuePieChart, setValuePieChart] = useState([])
    const [labelsPieChart, setlabelsPieChart] = useState([])
    const [layoutPieChart, setLayoutPieChart] = useState([])


    const [layoutPieChart2, setLayoutPieChart2] = useState([])
    const [valuePieChart2, setValuePieChart2] = useState([])
    const [labelsPieChart2, setlabelsPieChart2] = useState([])

    const [valueTable, setValueTable] = useState([])
    const [layoutTable, setLayoutTable] = useState([])

    useEffect(() => {
    

    axios.get("http://150.165.167.59:5000/graficos-relatorio").then(response => {
        console.log(response.data.files)
        setValuePieChart(response.data.files[0].data[0].values)
        setlabelsPieChart(response.data.files[0].data[0].labels)
        setLayoutPieChart(response.data.files[0].layout.title)

        setValuePieChart2(response.data.files[2].data[0].values)
        setlabelsPieChart2(response.data.files[2].data[0].labels)
        setLayoutPieChart2(response.data.files[2].layout.title)

        setValueTable(response.data.files[1].data[0].cells.values)
        setLayoutTable(response.data.files[1].data[0].header.values)
        
       /* if(valuePieChart == null){
        document.getElementById("secound-sheet").style.display = 'none'
        document.getElementById("third-sheet").style.display = 'none'
        document.getElementById("fourth-sheet").style.display = 'none'
        document.getElementById("no-graph-sheet").style.display = 'block'
       } */
        
        
    }).catch(function (error) {
        console.log(error);
    })
     axios.get("http://150.165.167.59:5000/graficos-relatorio-perifericos").then(response => {
        console.log(response.data.files)
        setFigura330(response.data.files[0])
        setFigura250(response.data.files[1])
        setFigura390(response.data.files[2])
        

    }).catch(function (error){
        console.log(error);
        document.getElementById('graficoPerifirico250').style.display = 'none'

        document.getElementById('graficoPerifirico390').style.display = 'none'
        
        document.getElementById('graficoPerifirico330').style.display = 'none'
    })
    axios.get("http://150.165.167.59:5000/graficos-relatorio-temporais").then(response => {
        console.log(response.data.files)
        setReset(response.data.files[0])
        setLoadCapacity(response.data.files[1])
        setMotorSpd(response.data.files[2])
        
    })
    
    axios.get("http://150.165.167.59:5000/graficos-relatorio-temporais2").then(response => {
        console.log(response.data.files)
        setSpeed_limits(response.data.files[0])
        setFence_open(response.data.files[1])
        
        
    }) 
    
      }, [])
      
   
    return(
        
        <div>

<div id="corpo">
    <div className="folha1">
        <div className="sectionOne" style={{display:'inline-block'}}>
                <div className="logoImg">
                <img alt="logo Ai Robots" src={logoAi}/>
            </div>
            
            <div className="logoImg2" >
                <img alt="logo fanuc" className="imgfanuc" src={logo2}/>
            </div>
        </div>
        <div>
            <h2 className="title">HEALTH CHECK REPORT</h2>
         </div>
         <div class="divBackImg">
            <img alt="background" className="imgBackground" src={background_image}/>
         </div>
    
        <div class="sectionTwo">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <strong>
                            Serial Number:
                            </strong>
                            
                        </td>
                        <td class="resposta">---</td>
                        
                    </tr>
                    
                </tbody>
                <tbody>
                    <tr>
                        <td>
                        <strong>
                        Robot Name:
                        </strong>
                        </td>
                        <td class="resposta">
                        Fanuc
                        </td>
                    </tr>
                    

                </tbody>
                <tbody>
                    <tr>
                        <td>
                        <strong>Robot Model: </strong>
                        </td>
                        <td class="resposta">
                        M70iC/50
                        </td>
                    </tr>
                    
                </tbody>
                <tbody>
                    <tr>
                        <td>
                        <strong>Robot Description: </strong>

                        </td>
                        <td class="resposta">---</td>

                    </tr>
                    
                </tbody>
                <tbody>
                    <tr>
                        <td>
                        <strong>
                        Company:
                        </strong>
                        </td>
                        <td class="resposta">

                        AiRobots
                        </td>
                    </tr>
                    
                </tbody>
                <tbody>
                    <tr>
                        <td>
                        <strong>
                             Unity Code:
                        </strong>
                        </td>
                        <td class="resposta">
                        ---
                            </td> 
                    </tr>
                    
                    

                </tbody>
                <tbody>
                    <tr>
                        <td>
                        <strong>
                        Created By:
                        </strong>
                        </td>
                       <td class="resposta">
                        ---
                        </td>
                    </tr>
                </tbody>
                <tbody>
                    <tr>
                        <td>
                        <strong>
                            Email:
                        </strong>
                        </td>
                       <td class="resposta">
                        ---
                            </td>
                    </tr>
                    
                </tbody>

            </table>

        </div>

    </div>

<div id="secound-sheet" class="folha2">
    <h3 class="t2">Robot Program Analysis</h3>
    <h5 class="text2">Here you will find the most common errors found in your robot program. The table explains the cause of each error and suggests a solution to fix it.</h5>
    <div class="graphDiv">
        
            <Plot
            data={[
              {type: "pie",
               values: valuePieChart,
               labels: labelsPieChart,
               textposition:"inside"

                
        }
            ]}
            layout={{title:layoutPieChart, width:850, height:600}}
            />
        
        
      </div>
     
</div>

<div id="third-sheet"class="folha2">
    <div class="graphDiv2">
    <Plot
            data={[
              {type: "pie",
               values: valuePieChart2,
               labels: labelsPieChart2,
               textposition:"inside"            
        }
            ]}
            layout={{title:layoutPieChart2, width:850, height:600}}
            />
    </div>

</div>

<div id="fourth-sheet" class="folha2">
    <div class="tabela">
    <Plot
                data={[
                {type: "table",
                    header:{values:[layoutTable[0],layoutTable[1],layoutTable[2],layoutTable[3]],
                        align: "center",
                        line: {width: 1, color: 'black'},
                        fill: {color: 'rgb(13, 20, 48)'},
                        font: {family: "Arial", size: 12, color: "white"}},
                    cells: { values:[
                        valueTable[0],valueTable[1],valueTable[2],valueTable[3]
                    ],align: "center",
                    line: {color: "black", width: 1},
                    font: {family: "Arial", size: 11, color: ["black"]}, 
                    fill: {color:['rgb(242, 242, 242)', 'white','white','white' ]}
                    }
                            
            }
                ]}
                layout={{width:1070, height:910}}
                />
</div>
   
    
</div>


 
 

<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={load_capacity.data}
            layout={load_capacity.layout}
            
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={motorSpd.data}
            layout={motorSpd.layout}
            
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={speed_limits.data}
            layout={speed_limits.layout}
            
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={fence_open.data}
            layout={fence_open.layout}
           
        />
    </div>
</div>

<div id="graficoPerifirico250" class="folhaPeriferico">
    <div class="graphDiv2">
        
            <Plot
            data={figura250.data}
            layout={figura250.layout}
       
        
    />
 
    </div>
</div>
 
 <div id="graficoPerifirico330" class="folhaPeriferico">
    <div class="graphDiv2">
        <Plot
           data={figura330.data}
           layout={figura330.layout}
        />
    </div>
</div> 

<div id="graficoPerifirico390" class="folhaPeriferico">
    <div class="graphDiv2">
        <Plot
            data={figura390.data}
            layout={figura390.layout}
        />
    </div>
</div> 

<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={reset.data}
            layout={reset.layout}
           
        />
    </div>
</div>
 
{/*
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={figura440.data}
            layout={figura440.layout}
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={figura450.data}
            layout={figura450.layout}
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={figura470.data}
            layout={figura470.layout}
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={figura480.data}
            layout={figura480.layout}
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={figura550.data}
            layout={figura550.layout}
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={figura560.data}
            layout={figura560.layout}
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={figura570.data}
            layout={figura570.layout}
        />
    </div>
</div>
<div class="folha2">
    <div class="graphDiv2">
        <Plot
            data ={figura580.data}
            layout={figura580.layout}
        />
    </div>
</div> */}
<div id="no-graph-sheet" class="folha2" style={{display:'none'}}>
    <div class="space"></div>
    <h5 class="text2">The report was not generated. Please go back to the main page and try again.</h5>
    <div class="space"></div>
</div>
<div class="space"></div>
</div>
        </div>
    )
}
export default Relatorio