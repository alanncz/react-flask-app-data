
import '../relatorio/styles.css'
import logoAi from '../../imagens/logoAi.png'
import logo2 from '../../imagens/pngegg.png'
import background_image from '../../imagens/background-TRANSP.png'


import Plot from 'react-plotly.js'
import { useEffect, useState } from 'react'
import axios from 'axios'


function Relatorio() {
    const [valuePieChart, setValuePieChart] = useState([])
    const [labelsPieChart, setlabelsPieChart] = useState([])
    const [layoutPieChart, setLayoutPieChart] = useState([])
    const [layoutPieChart2, setLayoutPieChart2] = useState([])
    const [layoutTable, setLayoutTable] = useState([])
    
    const [valuePieChart2, setValuePieChart2] = useState([])
    const [labelsPieChart2, setlabelsPieChart2] = useState([])
    const [valueTable, setValueTable] = useState([])
    
    useEffect(() => {

	axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*';
    axios.get("http://localhost:5000/graficos-relatorio").then(response => {
        
        console.log(response.data)
        setValuePieChart(response.data.files[0].data[0].values)
        setlabelsPieChart(response.data.files[0].data[0].labels)
        setLayoutPieChart(response.data.files[0].layout.title)

        setValuePieChart2(response.data.files[2].data[0].values)
        setlabelsPieChart2(response.data.files[2].data[0].labels)
        setLayoutPieChart2(response.data.files[2].layout.title)
        setValueTable(response.data.files[1].data[0].cells.values)
        setLayoutTable(response.data.files[1].data[0].header.values)
        
        
        // console.log(valueTable[0])
    })
    console.log(valueTable)
    console.log(layoutTable)
    
        // fetch('127.0.0.1:5000/relatorio').then(response => {
        //     console.log(response.json)
        //   response.json().then(data => {
        //     setData(data) 
        //   })
        // }).catch(erro => {
        //   console.error(erro)
        // })
      }, [])
   

    return(
        
        <div>

<body id="corpo">
    <div class="folha1">
        <div class="sectionOne" style={{display:'inline-block'}}>
                <div class="logoImg">
                <img src={logoAi}/>
            </div>
            
            <div class="logoImg2" >
                <img class="imgfanuc" style={{}} src={logo2}/>
            </div>
        </div>
        <div>
            <h2 class="title">HEALTH CHECK REPORT</h2>
         </div>
         <div class="divBackImg">
            <img class="imgBackground" src={background_image}/>
         </div>
    
        <div class="sectionTwo">
            <table>
                <tr>
                    <td>
                        <strong>
                         Serial Number:
                        </strong>
                    </td>
                    <td class="resposta">
                        ---
                    </td>
                </tr>
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
                <tr>
                    <td>
                        <strong>Robot Model: </strong>
                    </td>
                    <td class="resposta">
                        M70iC/50
                    </td>
                </tr>
                <tr>
                    <td>
                          <strong>Robot Description: </strong>

                    </td>
                    <td class="resposta">
                       ---
                    </td>
                </tr>
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

            </table>

        </div>

    </div>

<div class="folha2">
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

<div class="folha2">
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

<div class="folha2">

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
                font: {family: "Arial", size: 11, color: ["black"]}
                }
                        
        }
            ]}
            layout={{width:1070, height:910}}
            />
    
</div>
<div class="space"></div>
</body>
        </div>
    )
}
export default Relatorio