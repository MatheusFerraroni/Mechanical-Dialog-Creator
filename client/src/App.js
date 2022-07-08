import React from 'react';
import axios from "axios";


class ApiMDC{
  constructor(base_url, key){
    this.base_url = base_url
    this.key = key

    this.api = axios.create({
      baseURL: this.base_url,
    });
  }

  async check_email(email){
    const url = this.base_url+"check_user";
    const dat = {
               email: email,
               server_key: this.key
    }

    return await axios({
      method: 'post',
      url: url,
      headers: {"Content-Type": "application/json"}, 
      data: dat
    })
    .then(function (response) {
      return response
    })
    .catch(function (error) {
      return error
    });
  }

  async create_account(email, name){
    const url = this.base_url+"add_user";
    const dat = {
               email: email,
               name: name,
               server_key: this.key
    }

    return await axios({
      method: 'post',
      url: url,
      headers: {"Content-Type": "application/json"}, 
      data: dat
    })
    .then(function (response) {
      return response
    })
    .catch(function (error) {
      return error
    });
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      server_url: "http://localhost:8888/",
      server_key: "1033b11e-ea82-11ec-8fea-0242ac120002",
      email: "mail@mail.com_",
      name: "",
      user_uid: "",

      step: "server_info",// server_info, user_info
      btn_label: "Próximo"
    };
    

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const name = target.name;

    this.setState({
      [name]: target.value
    });
  }

  render() {
    if (this.state.step==="server_info"){
      return this.render_server_info()
    }else if (this.state.step==="user_info_criar"){
      return this.render_user_info_new_user()
    }else if (this.state.step==="user_info_confirmar_old"){
      return this.render_user_info_old_user()
    }
  }

  handleSubmit(event) {
    event.preventDefault();
    

    if (this.state.step==="server_info"){
        const api = new ApiMDC(this.state.server_url, this.state.server_key)
        const dis = this;
        api.check_email(this.state.email).then(function(resp){
          if(resp.status===200){
            if(resp.data.status){
              dis.setState({'user_uid': resp.data.uid})
              dis.setState({'name': resp.data.name})
              dis.enable_confirm_account();
            }else{
              dis.enable_create_account();
            }
          }else{
            alert("Not able to connect with credentials and endpoint.")
          }
        })
    }else if(this.state.step==="user_info_confirmar_old"){
      this.access_chat()
    }else if(this.state.step==="user_info_criar"){
      this.create_account()
    }
  }

  create_account(){
    const api = new ApiMDC(this.state.server_url, this.state.server_key)
    const dis = this;
    api.create_account(this.state.email, this.state.name).then(function(resp){
      if(resp.status===200){
        if(resp.data.status==="user_created"){
          dis.setState({'user_uid': resp.data.uid})
          dis.access_chat()
        }else{
          alert("Something went wrong. Check console for more informations")
          console.error(resp)
        }
      }else{
        alert("Not able to connect with credentials and endpoint.")
      }
    })
  }

  access_chat(){
    let params = "/chat?"
    params += "server_url="+this.state.server_url+"&"
    params += "server_key="+this.state.server_key+"&"
    params += "email="+this.state.email+"&"
    params += "name="+this.state.name+"&"
    params += "user_uid="+this.state.user_uid
    window.location = window.location.origin+params
  }

  enable_confirm_account(){
    this.setState({'name': 'nome nomenome'})
    this.setState({'btn_label': 'Acessar'})
    this.setState({'step': 'user_info_confirmar_old'})
  }

  enable_create_account(){
    this.setState({'step': 'user_info_criar'})
    this.setState({'btn_label': 'Criar e Acessar'})
  }

  render_server_info(){
    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <div className="px-8 py-6 mt-4 text-left bg-white shadow-lg w-96">
                <h3 className="text-2xl font-bold text-center">Account and Server</h3>
                <form onSubmit={this.handleSubmit}>
                    <div className="mt-4">
                        <div>
                            <label className="block">Email</label>
                                    <input
                                      type="text"
                                      placeholder="Email"
                                      className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600"
                                      name="email"
                                      value={this.state.email}
                                      onChange={this.handleInputChange}
                                      />
                        </div>
                        <div className="mt-4">
                            <label className="block">Server Endpoint</label>
                                    <input
                                      type="text"
                                      placeholder="Email"
                                      className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600"
                                      name="server_url"
                                      value={this.state.server_url}
                                      onChange={this.handleInputChange}
                                      />
                        </div>
                        <div className="mt-4">
                            <label className="block">Server Key</label>
                                    <input
                                      type="text"
                                      placeholder="Email"
                                      className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600"
                                      name="server_key"
                                      value={this.state.server_key}
                                      onChange={this.handleInputChange}
                                      />
                        </div>
                        <div className="">
                            <input
                              className="px-6 py-2 mt-4 text-white bg-blue-600 rounded-lg hover:bg-blue-900 float-right"
                              type="submit"
                              value={this.state.btn_label}
                              />
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
  }


  render_user_info_new_user(){
    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <div className="px-8 py-6 mt-4 text-left bg-white shadow-lg w-96">
                <h3 className="text-2xl font-bold text-center">Usuário</h3>
                <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative text-center mt-3" role="alert">
                  <span className="block sm:inline">Usuário não encontrado.</span>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <div className="mt-4">
                        <div>
                            <label className="block">Nome</label>
                                    <input
                                      type="text"
                                      placeholder="Nome"
                                      className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600"
                                      name="name"
                                      value={this.state.name}
                                      onChange={this.handleInputChange}
                                      />
                        </div>
                        <div className="">
                            <input
                              className="px-6 py-2 mt-4 text-white bg-blue-600 rounded-lg hover:bg-blue-900 float-right"
                              type="submit"
                              value={this.state.btn_label}
                              />
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
  }

  render_user_info_old_user(){

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <div className="px-8 py-6 mt-4 text-left bg-white shadow-lg w-96">
                <h3 className="text-2xl font-bold text-center">Usuário</h3>
                <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative text-center mt-3" role="alert">
                  <span className="block sm:inline">Usuário encontrado! <br/> Confirme seus dados.</span>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <div className="mt-4">
                        <div>
                            <label className="block">Nome</label>
                                    <input
                                      type="text"
                                      placeholder="Nome"
                                      className="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600"
                                      name="name"
                                      value={this.state.name}
                                      disabled
                                      />
                        </div>
                        <div className="">
                            <input
                              className="px-6 py-2 mt-4 text-white bg-blue-600 rounded-lg hover:bg-blue-900 float-right"
                              type="submit"
                              value={this.state.btn_label}
                              />
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
  }
}

export default App;
