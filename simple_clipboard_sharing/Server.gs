var scriptProperties = PropertiesService.getScriptProperties()

function doGet(e) {
  var param = e.parameter;
  if(param.k=="{{your very own very strong password}}") {
    var clipboard_text=scriptProperties.getProperty("cp");
    if(clipboard_text!=null) {
      return ContentService.createTextOutput(clipboard_text); 
    }
  }
  return ContentService.createTextOutput('{"failure":"KeyError"}').setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  var param = e.parameter;
  if(param.k=="{{your very own very strong password}}") {
    if(param.cp) {
      scriptProperties.setProperty("cp", param.cp);
      return ContentService.createTextOutput('{"status":"success"}').setMimeType(ContentService.MimeType.JSON); 
    }
  }
  return ContentService.createTextOutput('{"status":"failure"}').setMimeType(ContentService.MimeType.JSON);
}
