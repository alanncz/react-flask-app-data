import '../../componentes/Header/styles.css'
import logo from '../../imagens/logo.svg' 
function Header(){
    return(
        <header id="header">
            <img className="logoAiRobots" src={logo} alt="LogoAiRobots"/>
        </header>
    )
}
export default Header;