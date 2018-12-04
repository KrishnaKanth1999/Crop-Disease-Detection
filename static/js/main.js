$(function() {
    $('#upload-file-btn').click(function() {
    $(".causes0").html('')
$(".causes1").html('')
$(".causes2").html('')
$(".causes3").html('')
$(".causes4").html('')
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                myfn(data)
                console.log('Success!');
            },
        });
    });

        $('.user_details').click(function() {
        form_data=JSON.stringify({"details":{"name":$(".name").val(),"mail":$(".mail").val(),"number":$(".number").val()}})
        console.log(form_data)
        $.ajax({
            type: 'POST',
            url: '/vendor',
            data: form_data,

                    contentType: "application/json; charset=utf-8",
            success: function(data) {
                console.log('Success!');
                activity(data)
            },
        });
    });


});

function activity(res)
{
console.log(res)
}

function myfn(res)
{

  data= ["Apple Scab","Apple Black Rot","Apple Rust","Apple Healthy","Cherry Powdery Mildew","Cherry Healthy", "Corn Cercospora Leaf","Corn Common Rust","Corn Healthy","Grapes Esca Black Measles","Grape Leaf Blight","Grape Healthy", "Peach Bacterial Spot","Peach Healthy","Pepper Bell Bacterial Spot","Pepper Bell Healthy","Potato Early Blight","Potato Late Blight","Strawberry Leaf Scorch","Strawberry Healthy"]



store={
  "Apple Scab": {
    "sym": "Dark velvet covering on leaves, Velvety olive-green to black spots on leaves",
    "cause": "Venturia inaequalis",
    "nc_c": "Use resistant varieties: Prima, Priscilla, Sir Prize, Jonafree, Red free, Dayton, Pristine, Goldrush, Enterprise or Liberty.",
    "c_c": "Use fungicide such as Captan."
  },
  "Apple Black Rot": {
    "sym": "Leaf spots with purple edge, tancenter",
    "cause": "Botryosphaeria obtusa",
    "nc_c": "Prune out dead wood in tree, mummified apples and shoots infected with fire blight, Remove piles of pruning from orchard and burn",
    "c_c": "Use fungicide such as Captan."
  },
  "Apple Rust": {
    "sym": "Yellow-orange to orange spots on leaves",
    "cause": "Gymnosporangium juniperi virginianae",
    "nc_c": "Use resistant varieties: Red Delicious, Jonafree, Liberty or Red free. Remove galls from cedar trees within 2 to 3 miles (usually not practical).",
    "c_c": "Use fungicide such as Ferbam. Begin spray applications at pink bud stage. Or, during early spring, monitor mature galls on cedars. Begin spray applications before rain causes gelatinous orange spikes (teliahorns) to form."
  },
  "Apple Healthy": {
    "sym": "  -  ",
    "cause": " - ",
    "nc_c": " - ",
    "c_c": " - "
  },
  "Cherry Powdery Mildew": {
    "sym": "Powdery mildew is marked by superficial, white, weblike growth on leaves, shoots, or fruit.",
    "cause": "Powdery mildew forms when plant foliage is dry, lighting is low, temperatures are moderate and there is high humidity",
    "nc_c": "By poring neem oil kind of natural pesticides,Since dry conditions coupled with high humidity are often the culprits behind powdery mildew growth, watering your plants overhead and getting the entire plant wet can help. ",
    "c_c": "Baking Soda with liquid soap and water,  "
  },
  "Cherry Healthy": {
    "sym": "  -  ",
    "cause": " - ",
    "nc_c": " - ",
    "c_c": " - "
  },
"Corn Cercospera Leaf": {
    "sym": "Symptoms seen on corn include leaf lesions, discoloration (chlorosis), and foliar blight. The fungus survives in debris of topsoil and infects healthy crop via asexual spores called conidia ",
    "cause": "It is a foliar fungal disease that affects maize, also known as corn.",
    "nc_c": "By removing weeds, above ground airflow to the crop is increased, relative humidity is decreased, and it limits infection at most susceptible times",
    "c_c": "Use fungicide such as Captan."
  },
  "Corn Common Rust": {
    "sym": "Circular to elongate golden brown or cinnamon brown, powdery, erumpent pustules appear on both leaf surface",
    "cause": "fungus Puccinia sorghi",
    "nc_c": "Neem , Salt Spray, Citrus Oil and Caynee Pepper",
    "c_c": "Plant hybrids like Deccan, Ganga-5, Deccan Hybrid Makka-103 and DHM - 1 which are resistant to this disease to minimise the disease intensity"
  },
  "Corn Healthy": {
    "sym": "  -  ",
    "cause": " - ",
    "nc_c": " - ",
    "c_c": " - "
  },
  "Grapes Esca Black Measles": {
    "sym": "Symptom appears on leaves, trunk, canes and berries. On leaves we will see intervenaial striping looks like tiger strips. White cultivars shows chlorotic and necrotic strips where as red cultivars shows red areas and necrotic strips",
    "cause": "Fungus",
    "nc_c": "Till date there is no effective method to control this disease. Remove the infected berries, leaves and trunk and destroy them. Protect the prune wounds to minimize fungal infection using wound sealant (5% boric acid in acrylic paint) or essential oil or suitable fungicides",
    "c_c": "Mantis EC Botanical 32-ounce Insecticide Miticide Concentrate, Monterey Garden 32-ounce Insect Spray with Spinosad Concentrate"
  },
  "Grape Leaf Blight": {
    "sym": "On leaf surface we will see lesions which are irregularly shaped (2 to 25 mm in diameter). Initially lesions are dull red to brown in color turn black later. If disease is severe this lesions may coalesce. On berries we can see symptom similar to black rot but the entire clusters will collapse",
    "cause": "Fungus",
    "nc_c": "Neem , Salt Spray, Citrus Oil and Caynee Pepper",
    "c_c": "Fungicides sprayed for other diseases in the season may help to reduce this disease."
  },
  "Grapes Healthy": {
   "sym": "  -  ",
    "cause": " - ",
    "nc_c": " - ",
    "c_c": " - "
  },
  "Peach Bacterial Spot": {
    "sym": "Symptoms of this disease include fruit spots, leaf spots, and twig cankers. Fruit symptoms include pitting, cracking, gumming, and watersoaked tissue, which can make the fruit more susceptible to brown rot, rhizopus, and other fungal infections. Severe leaf spot infections can cause early defoliation",
    "cause": "nectarines, apricots, and plums caused by Xanthomonas campestris pv. pruni.",
    "nc_c": "Neem , Salt Spray, Citrus Oil and Caynee Pepper",
    "c_c": "As a result, foliar injury on the oldest leaves is normal and expected when using repeated copper applications as it indicates the copper is working to control the bacterial spot pathogen. However, excessive injury can occur when the copper becomes more soluble, such as during slow drying (rainy) conditions and when applied in an acidic solution"
  },
  "Peach Healthy": {
    "sym": "  -  ",
    "cause": " - ",
    "nc_c": " - ",
    "c_c": " - "
  },
  "Pepper Bell Bacterial Spot": {
    "sym": "Bacterial leaf spot causes lesions on the leaves that look as though they are soaked with water. These lesions normally begin on the lower leaves. As the disease progresses, it leaves a dark, purple-brown spot with a light brown center.",
    "cause": "The bacterium Xanthomonas campestris pv. vesicatoria causes bacterial leaf spot. It thrives in areas with hot summers and frequent rainfall. The bacterium is spread by plant debris in the soil and through infected seeds.",
    "nc_c": "A minimum of a one year rotation away from pepper and other solanaceous crops is highly recommended, with a thee year rotation preferred. Growers should also avoid planting pepper, tomato, eggplant, and potatoes close to each other during the season.",
    "c_c": "Monterey Garden 32-ounce Insect Spray with Spinosad Concentrate, Southern Ag 8-ounce Natural Concentrate"
  },
  "Pepper Bell Healthy": {
    "sym": "  -  ",
    "cause": " - ",
    "nc_c": " - ",
    "c_c": " - "
  },

  "Potato Early Blight": {
    "sym": "It can be found in all potato growing areas. Symptoms of early blight are easily confused with those of brown leaf spot. Early blight can be differentiated by the larger lesions and presence of concentric rings within the lesion.",
    "cause": "Early blight on potato is caused by the fungapathogen Alternaria solan",
    "nc_c": "Avoid over irrigation, allowing leaf tissue to fully dry.Use of tillage practices to bury plant debris also reduces inoculum. Fungicide programs are the most effective means to control the disease",
    "c_c": "Use fungicide such as Captan."
  },
  "Potato Late Blight": {
    "sym": "The disease often appears following periods of very wet weather. On very young leaves, irregular, water-soaked lesions appear. Lesions are dark brown to black and can appear small at first",
    "cause": "Phytophthora infestans is an oomycete or water mold, a microorganism that causes the serious potato and tomato disease known as late blight or potato blight",
    "nc_c": "Good field drainage and proper plant spacing for optimal air movement are desirable. Proper sanitation is necessary: destroy cull piles, volunteers, and any infected material, Deeply till the garden bed in late fall. Disrupting the soil prevents blight spores from having an undisturbed place to spend the winter",
    "c_c": "Monterey Garden 32-ounce Insect Spray with Spinosad Concentrate, Southern Ag 8-ounce Natural Concentrate"
  },
  "Strawberry Leaf Scorch": {
    "sym": " This disease produces small purple spots that first appear on older leaves and gradually enlarge, join other spots and finally produce large dead patches giving the leaves a scorched appearance ",
    "cause": "Leaf scorch is common on older leaves and at the end of a season, but can also affect leaf stalks, fruit stalks, flowers, and fruit. ",
    "nc_c": "Neem , Salt Spray, Citrus Oil and Caynee Pepper",
    "c_c": "1. Avoid overhead irrigation if possible.2. Remove and burn older infected leaves and trash from previous crops near to the new plantings.3. Practice crop rotation."
  },
  "Strawberry Healthy": {
    "sym": "  -  ",
    "cause": " - ",
    "nc_c": " - ",
    "c_c": " - "
  }
}


name=data[res].toString()

console.log(store[name])
$(".causes0").append(name)
$(".causes1").append(store[name].sym)
$(".causes2").append(store[name].cause)
$(".causes3").append(store[name].nc_c)
$(".causes4").append(store[name].c_c)
}


