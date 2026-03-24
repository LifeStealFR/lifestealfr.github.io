window.addEventListener("message",event=>{
    let data = event.data;
    if(data && data.download) {
        console.log(data.download);
        let name = data.name || `download.zip`;
        var zip = new JSZip();
        for (const [key, value] of data.download.entries()) {
            if(typeof value == "string") {
                console.log(`String: ${key} => ${value}`);
                zip.file(key,value);
            }else if(typeof value == "object") {
                if(value.type == "base64" && typeof value.content == "string") {
                    console.log(`Object: ${key} => ${JSON.stringify(value,null,2)}`);
                    zip.file(key,value.content, {base64: true});
                }else{
                    console.log(`Object [Malformed]: ${key} => ${JSON.stringify(value,null,2)}`);
                }
            }else{
                console.log(`Unknown type: ${key} => ${value}`);
            }
        }
        zip.generateAsync({type:"blob"})
            .then(function(blob) {
              saveAsLegacy(blob, name);
            });
    }
    function saveAsLegacy(content, filename) {
      const link = document.createElement('a');
      link.href = URL.createObjectURL(content);
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(link.href); // Clean up
    }
})