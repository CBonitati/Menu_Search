ingredients = ["Vegetarian Options", "Vegan Options", "Peanut Allergy", "Lactose Intolerance", "Celiac Disease (Gluten Free)", "Kosher", "Eggs"];
var gen_label, checkbox, formdiv, br;
var table = document.getElementById("choice_table");
formdiv = document.getElementsByClassName("checkbox_section")[0];
for (var x = 0; x < ingredients.length; x++) {
  gen_label = document.createElement("label");
  gen_label.className = "ing_label";
  gen_label.innerHTML = ingredients[x];
  checkbox = document.createElement("input");
  checkbox.setAttribute("type","checkbox");
  checkbox.setAttribute("name","you_decide");
  checkbox.className = "ing_box";
  var row = document.createElement("tr");
  var label_td = document.createElement("td");
  var checkbox_td = document.createElement("td");
  label_td.appendChild(gen_label);
  checkbox_td.appendChild(checkbox);
  row.appendChild(label_td);
  row.appendChild(checkbox_td);
  table.append(row);
}

