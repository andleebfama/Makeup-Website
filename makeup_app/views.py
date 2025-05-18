from django.shortcuts import render, redirect
from .forms import PurchaseInquiryForm
from .forms import ContactForm
# Create your views here.

def index(request):
    x = {
        'name': 'Andleeb suman sehar'
    }
    return render(request, 'index.html', {'x': x})


from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'signin.html', {'error': 'User not found.'})

        user = authenticate(request, username=user_obj.username, password=password)
        if user:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'signin.html', {'error': 'Invalid password.'})
    
    return render(request, 'signin.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def purchase_view(request):
    initial_data = {
        'product': request.GET.get('product', ''),
        'price': request.GET.get('price', '')
    }

    if request.method == 'POST':
        form = PurchaseInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')  # Create a thank_you.html
    else:
        form = PurchaseInquiryForm(initial=initial_data)

    return render(request, 'purchase.html', {'form': form})

def home(request):
    query = request.GET.get('q', '').lower()

    all_products = [
        {"name": "Set of Foundations", "price": "Rs.3500", "image": "https://www.lorealparisusa.com/-/media/project/loreal/brand-sites/oap/americas/us/beauty-magazine/2023/10-october/10-18/makeup-with-skin-care-benefits/a-collage-of-loreal-paris-makeup-skin-care-hybrid-products.jpg?rev=06287abe8ced4a7387b58857e7469345&cx=0.51&cy=0.51&cw=2000&ch=815&hash=39CA1A68410D4DF70B4220BE0970EE4F4A81C853"},
        {"name": "Lipgloss", "price": "Rs.670", "image": "https://www.boddess.com/pub/media/catalog/product/cache/bd4544c7fbee46d953477c2a1c9ae0ef/1/0/10_2.png"},
        {"name": "Brushes and Lipsticks", "price": "Rs.450", "image": "https://pics.craiyon.com/2023-10-10/76e6007e6ac940ae978f3604073ff095.webp"},
        {"name": "Blush on", "price": "Rs.900", "image": "https://media.self.com/photos/57dc14dbbcf2c5c50b7d004a/master/pass/makeup-skin-tone-nars-orgasm-blush.jpg"},
        {"name": "Set of lipsticks", "price": "Rs.789", "image": "https://lotshop.pk/cdn/shop/collections/makeup-products-210058.jpg?v=1730734281"},
        {"name": "Mascara", "price": "Rs.9000", "image": "https://www.maybelline.com/-/media/project/loreal/brand-sites/mny/americas/us/makeup-tips/jenna-kristinas-picks-for-the-best-drugstore-makeup-products/product_laydown_lashsensational_us_4_dmi_image_na_no-cta.jpg?rev=dfe142eadcad4aa5a846e6ab02c0fe52&cx=0.25&cy=0.31&cw=1080&ch=607&hash=047C725781C301C8C66EF180ADCED316"},
        {"name": "Eyeshadow Pallete", "price": "Rs.3409", "image": "https://beautyglazedpk.com/cdn/shop/products/image_00151337-7d52-40f5-81d7-faf49ad22651_1200x1200.jpg?v=1646437205"},
        {"name": "Gloss and liners", "price": "Rs.11000", "image": "https://glowbeauty.pk/cdn/shop/files/muicin-germany-makeup-kits-muicin-9-in-1-everyday-professional-makeup-kit-40579555066113_1600x.jpg?v=1706414404"},
        {"name": "Lipsticks", "price": "Rs.11000", "image": "https://rivaj-uk.com/cdn/shop/files/Pure-Matte-01-1.jpg?v=1715023499&width=320"},
        {"name": "Foundations", "price": "Rs.567", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLKLe_6vHWhLrYutO3UvmikeHTtn8XIb-TKQ&s"},
        {"name": "Brushes", "price": "Rs.1289", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqRHdt01V5RkQNNgAXBiKLV1-fOrFyXYfUMA&s"},
        {"name": "Perfumes", "price": "Rs.9078", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGWJo2rh438GUj7E8nH1oCN0XqjM1H4P3Qbw&s"},
        {"name": "Gloss", "price": "Rs.1234", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWhgwe7vACcoDZqpYr3CE41iNshOjCTqBnFA&s"},
        {"name": "Brush", "price": "Rs.9846", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_pBhDv_ZpfeN43F5ERUGfW-4bJCXGSZseLw&s"},
        {"name": "Blush on", "price": "Rs.1209", "image": "data:image/jpeg;base64,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"},
        {"name": "NailPaint", "price": "Rs.9846", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX3mq4I815Rkmtuo9uVTfAMs1_0j5xW_KwbA&s"},
        {"name": "lipstick n blush", "price": "Rs.1233", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRfX2r4eXF5PgE8upnjaO-XuAm_yzCe3LL5Q&s"},
        {"name": "Eye set", "price": "Rs.6754", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRE7kbckmz4vYzXY8-hkdwEcb_phGUmF-Hfgg&s"},
        {"name": "Makeup set", "price": "Rs.7890", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQK_ZRIU7BL2jnXhS_UVk_DegTJCfsE5FsfSg&s"},
        {"name": "Kit", "price": "Rs.1245", "image": "https://w7.pngwing.com/pngs/776/841/png-transparent-assorted-brand-labeled-makeup-products-cosmetics-beauty-makeup-brush-make-up-artist-women-cosmetics-miscellaneous-women-accessories-indian-nude-women.png"},
    
    ]

    sale_products = [p for p in all_products if "lipstick" in p["name"].lower() or "brush" in p["name"].lower() or "blush on" in p["name"].lower() ]

    if query:
        products = [p for p in all_products if query in p["name"].lower()]
    else:
        products = all_products

    feedbacks = [
        {"name": "Alaina", "image": "https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&h=100", "rating": 5, "review": "Nice experience."},
        {"name": "Jennifer", "image": "https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg?auto=compress&cs=tinysrgb&h=100s", "rating": 4, "review": "Very good experience."},
        {"name": "Alexa", "image": "https://images.pexels.com/photos/1130626/pexels-photo-1130626.jpeg?auto=compress&cs=tinysrgb&h=100", "rating": 5, "review": "Highly recommend!"},
        ]

    return render(request, 'home.html', {
        'products': products,
        'sale_products': sale_products,
        'feedbacks': feedbacks,
        'query': query,
    })

def category(request):
    categories = [
        {"name": "Foundation", "image_url": "https://www.chanel.com/images/t_one/w_0.43,h_0.43,c_crop/q_auto:good,f_jpg,fl_lossy,dpr_1.2/w_1920/b10-1-35fl-oz--packshot-default-147130-8835363700766.jpg"},
        {"name": "Lipstick", "image_url": "https://netstorage-briefly.akamaized.net/images/904253bb0958a15a.jpg?imwidth=900"},
        {"name": "Eyeliner", "image_url": "https://media.naheed.pk/catalog/product/cache/2f2d0cb0c5f92580479e8350be94f387/1/1/1195455-1.jpg"},
        {"name": "Brushes", "image_url": "https://miniso.pk/cdn/shop/files/6941447509074-1.jpg?v=1683265289"},
        {"name": "Eyeshadow", "image_url": "https://revolutionbeauty.pk/cdn/shop/products/MakeupRevolutionForeverFlawlessAllureEyeshadowPalette4.jpg?v=1744784007"},
        {"name": "Mascara", "image_url": "https://www.makeupcityshop.com/cdn/shop/products/3616301261902_9bbcdf80-140d-4bea-aef1-68b7ed9b2338.jpg?v=1694517094"},
        {"name": "Blush", "image_url": "https://derma.pk/wp-content/uploads/2024/03/DERMA.PK-71.webp"},
        {"name": "Highlighter", "image_url": "https://christinecosmetics.ae/cdn/shop/products/Professional_Highlighter_Palette_1024x1024.png?v=1737059994"},
        {"name": "Concealer", "image_url": "https://sdcdn.io/cl/cl_sku_Z9FF06_3000x3000_0.jpg?height=700px&width=700px"},
    ]
    return render(request, 'category.html', {'categories': categories})
def category_detail(request, category_name):
    dummy_images = {
        "Foundation": [
           {"url":"http://media.allure.com/photos/5771addb3b5256713da4c394/master/pass/beauty-trends-blogs-daily-beauty-reporter-2016-04-25-liquid-foundations.jpg","price": "RS.2000"},
            {"url":"https://www.makeup.com/product-and-reviews/foundation/'/-/media/project/loreal/brand-sites/mdc/americas/us/articles/2019/05_may/15-best-matte-foundations/matte-foundations-to-add-to-your-stash-hero-mudc-051619.jpg?w=600&h=450&blr=False&hash=81925077F05805916C68595492365048%27","price": "RS.4500"},
            {"url":"https://www.chanel.com/images/t_one/w_0.43,h_0.43,c_crop/q_auto:good,f_jpg,fl_lossy,dpr_1.2/w_1920/b10-1-35fl-oz--packshot-default-147130-8835363700766.jpg","price": "RS.1590"}
        ],
        "Lipstick": [
            {"url":"https://i5.walmartimages.com/asr/7deb27ab-38db-4282-aedd-d6490f065495.c9ef29bdfce901f188dc4743396b63b1.jpeg","price": "RS.1220"},
            {"url":"https://hips.hearstapps.com/bpc.h-cdn.co/assets/17/30/smashbox-be-legendary-matte-lipstick.jpg?crop=1xw:1.0xh;center,top&resize=768:*","price": "RS.1050"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUNSTPQaNFHkVQokqwrJVfFpiStF4KgU3SaV-ehAO200kdV-sTAuIp2EHbVirJ-sdh1Ak&usqp=CAU","price": "RS.920"},
        ],
        "Eyeliner": [
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYamZ9986orI0q5BDn6UeSQ3hh2PeDgBzTnA&s","price": "RS.330"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKE418liTv-2T98-iuEFCgzVCNxXtPih_ozWB19iUMCKV76Ji7BLdB0u9XMiHKktcHBoQ&usqp=CAU","price": "RS.600"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAtUO7x5dL_kf_rEwYYyEJfirN9l82I_9ysA&s","price": "RS.455"},
        ],
        "Brushes": [
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqh1q5VvoNP4pCIIb1tuXuM4n2CgxgO8v-XQ&s","price": "RS.200"},
           {"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEhSqaFwRpowh6vmPRO6yqoNRKtY6laIdNPeZUuF8zszM_C6QWWxlVo3smwk2CtdLImCw&usqp=CAU","price": "Rs.500"},
           {"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpNuV2oWJQloXnqbgWF6Tg-fmZeqVD4iPYYQ&s","price": "RS.820"},
        ],
        "Eyeshadow": [
            {"url":"https://rivaj-uk.com/cdn/shop/products/HDFlawlessShadowPalletemainimage.jpg?v=1745997695","price": "RS.1220"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuuwTSwo2InMMSTNOaynaewXcy6Vk5qL8-EQ&s","price": "RS.960"},
            {"url":"https://www.ubuy.com.pk/productimg/?image=aHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0kvODFrRkdaR2tKOEwuX1NMMTUwMF8uanBn.jpg","price": "RS.2230"},
        ],
        "Mascara": [
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbWeGNDWIyJ6jkuUsgijgQoZwCqh6RqFWyIg&s","price": "RS.200"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlIArYxxCsjTMY3RApH6_jv0yhkgFWfKnIZw&s","price": "RS.900"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkjmVL_nbLV8x05VMRJbmEnxzGxv0pSTWMoQ&s","price": "RS.250"},
        ],
        "Blush": [
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRH_KRHYipGUVWS6TOAtV6Iippw2G17mhhdrg&s","price": "RS.450"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt-sk6xymKz6LdSi-bRuAWfi37ytZOrL9Zmw&s","price": "$20"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1CP1vwLT_Qbfj1UNxW31aLfhh6Clo8Zw1Aw&s","price": "$20"},
        ],
        "Highlighter": [
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmLXm4SyF24798AMcDIXQSeqC1h4k2jLFvsw&s","price": "RS.320"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGbXf44y0sdMpYYFrOdVHn4HeiJXfY9se00A&s","price": "RS.900"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5kIf27DcbfMNm3pvf7VZSrRgHdr-e1E8IrA&s","price": "RS.450"},
        ],
        "Concealer": [
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZsHecCEtPossBjWu4iRKw5IEaVxuaXIpMxQaHPUIRbsfbNtA2AdeuyXqe65B2ZocwkBI&usqp=CAU","price": "RS.780"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQr5YT0DGz91bst5saVg41Ppk7XnZJ_dvBG2A&s","price": "RS.890"},
            {"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpHfLHcLafaCBc53Yi2FlKIkmBx_widwNLUxNVLkAePvSr8RAd9gvseuInjRcxORIHpfw&usqp=CAU","price": "RS.550"},
        ]
    }

    images = dummy_images.get(category_name, [])[:3]
    return render(request, 'category_detail.html', {'category_name': category_name, 'images': images})


# views.py
def products_view(request):
    products = [
        {
            'name': 'Set of Foundations',
            'price': 'RS.3500',
            'image': 'https://www.lorealparisusa.com/-/media/project/loreal/brand-sites/oap/americas/us/beauty-magazine/2023/10-october/10-18/makeup-with-skin-care-benefits/a-collage-of-loreal-paris-makeup-skin-care-hybrid-products.jpg',
        },
        {
            'name': 'Lipgloss',
            'price': 'RS.670',
            'image': 'https://www.boddess.com/pub/media/catalog/product/cache/bd4544c7fbee46d953477c2a1c9ae0ef/1/0/10_2.png',
        },
        {
            'name': 'Eyeshadow Palette',
            'price': 'RS.3409',
            'image': 'https://beautyglazedpk.com/cdn/shop/products/image_00151337-7d52-40f5-81d7-faf49ad22651_1200x1200.jpg?v=1646437205',
        },
    ]
    return render(request, 'products.html', {'products': products})

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')  # Optional thank-you page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



