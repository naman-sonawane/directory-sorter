import React, {useState, useEffect} from 'react'

function App() {
  const createFolder = async(e) => {
    e.preventDefault()
    const form = new FormData(e.target)
    const jsondata = Object.fromEntries(form.entries())
    const response = await fetch("/createfolder", {method:"POST", headers:{"Content-Type":"application/json"},
    body: JSON.stringify({"path":jsondata.path})})
    
    const data = await response.json();
    document.getElementById("messageBox").innerHTML = data.msg

  }

  const [data, setData] = useState([{}])

  useEffect(() => {
    //Pass
  }, [])
  
  return (
    <div className="flex justify-center items-center h-screen bg-gradient-to-br from-cyan-400 to-blue-500">
      <div className="text-center p-20 bg-red-100 rounded-xl bg-gradient-to-br from-cyan-300 to-blue-400 border-white border-opacity-40 border-2">
        <h1 className="font-bold text-3xl text-gray-800">Simplistic Directory Sorter</h1>
        <h5 className="font-medium text-l pb-10 text-gray-700">Enter a directory to sort, then hit submit.</h5>

        <form onSubmit={createFolder}>
          <div className="mb-4">
            <input name="path" className="px-3 py-2 rounded-md w-3/4 outline-gray-300 hover:shadow-white hover:outline-blue-500 hover:transition-all hover:duration-700 hover:ease-in-out transition-all duration-700 ease-in-out" placeholder="Path" />
          </div>
          <button type="submit" className="hover:transition hover:duration-700 hover:ease-in-out bg-gradient-to-br from-blue-500 to-blue-700 hover:from-blue-600 hover:to-blue-800 mt-6 text-white font-bold py-2 px-4 rounded">
            Submit
          </button>
        </form>
        <h5 id="messageBox" className="font-medium text-l pt-4 text-gray-700"></h5>
        <h5 className="font-normal text-base pt-4 text-gray-800">Made with React + Flask ✨</h5>
        <h5 className="font-normal text-sm text-gray-800">Naman Sonawane</h5>
      </div>
    </div>
  );
  }
export default App