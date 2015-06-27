from flask import Flask, render_template
from make_logo import generate
import random

app = Flask(__name__)

def get_fonts():
    fonts = "Questrial|Rambla|Alegreya Sans SC|Alfa Slab One|Source Sans Pro|Nixie One|Glegoo|Dosis|Abel|Bubblegum Sans|Patrick Hand|Fira Sans|Crafty Girls|Noto Sans|Domine|Droid Sans|Cantata One|Permanent Marker|Just Another Hand|Jockey One|Signika Negative|Lato|Arvo|Antic Slab|Cabin|Playfair Display|Fauna One|ABeeZee|BenchNine|Viga|Neuton|Sorts Mill Goudy|Economica|News Cycle|Michroma|Lora|Niconne|PT Sans|Poiret One|Acme|Armata|Cherry Cream Soda|Syncopate|PT Sans Narrow|Ropa Sans|Cabin Condensed|Tinos|Philosopher|Bad Script|Istok Web|Arimo|Quicksand|Paytone One|Oleo Script|Noto Serif|Ubuntu|Gudea|Marck Script|Droid Sans Mono|Montserrat Alternates|Josefin Sans|Bitter|Carrois Gothic|PT Serif|Limelight|Lobster|Gentium Basic|Kreon|Fugaz One|Waiting for the Sunrise|Monda|Reenie Beanie|Anton|Crete Round|Shadows Into Light|Rokkitt|Josefin Slab|Fredoka One|Russo One|Libre Baskerville|Copse|Racing Sans One|Walter Turncoat|Sigmar One|Source Code Pro|Gloria Hallelujah|Fontdiner Swanky|Calligraffitti|Exo|Asap|Tangerine|Days One|Cantarell|Antic|Muli|Great Vibes|Alegreya Sans|Ubuntu Condensed|EB Garamond|Droid Serif|Molengo|Jura|Allerta|Dancing Script|Montserrat|Electrolize|Architects Daughter|Open Sans|Open Sans Condensed:300|Coda|Actor|Merriweather|Varela|Didact Gothic|Chewy|Berkshire Swash|Scada|Orbitron|Abril Fatface|Titillium Web|Bangers|Roboto Condensed|Ruda|Marvel|Merriweather Sans|Sanchez|Enriqueta|Changa One|Archivo Narrow|Oxygen|Archivo Black|Hind|Vollkorn|Nobile|Passion One|Patua One|Audiowide|Hammersmith One|Cookie|Nunito|Quattrocento Sans|Pinyon Script|Sacramento|Exo 2|Ultra|Raleway|Amiri|Vidaloka|Slabo 27px|Kaushan Script|Roboto|Inconsolata|Pacifico|Righteous|Carme|Squada One|Julius Sans One|Signika|Cuprum|Source Serif Pro|PT Sans Caption|Lusitana|Courgette|Shadows Into Light Two|Homenaje|Play|Noticia Text|Black Ops One|IM Fell English|Indie Flower|Alegreya|Yanone Kaffeesatz|Comfortaa|Homemade Apple|Old Standard TT|Share|Cutive|Advent Pro|Sintony|Playball|Roboto Slab|Goudy Bookletter 1911|Pathway Gothic One|Karla|Playfair Display SC|Oswald|Quattrocento|Maven Pro|Alice|Amatic SC|Special Elite|Satisfy|Basic|Bree Serif|Coming Soon|Damion|Bevan|Amaranth|Pontano Sans|Varela Round|Francois One|Fjalla One|Volkhov|Crimson Text|Doppio One|Chivo|Voltaire|Luckiest Guy|Cardo|Gentium Book Basic|Covered By Your Grace|Handlee|Rock Salt|Nothing You Could Do|Lobster Two|Cinzel"
    return fonts.split("|")

def format_data(data):
    return '"%s"' %('","'.join(data))


def update_graphic(current_font,color,color_hidden,hidden):

    fonts = get_fonts()
    letters, colors, xcoords, ycoords = generate(hidden=hidden,
                                                 color=color,
                                                 color_hidden=color_hidden)
 
    # Format for d3 input
    letters = format_data(letters)
    colors = format_data(colors)
    xcoords = format_data([str(x) for x in xcoords])
    ycoords = format_data([str(x) for x in ycoords])

    return render_template('generate.html',fonts=fonts, 
                                           current_font=current_font,
                                           letters=letters,
                                           colors=colors,
                                           xcoords=xcoords,
                                           ycoords=ycoords,
                                           color=color,
                                           color_hidden=color_hidden,
                                           current_text=hidden)

@app.route('/')
def new_logo():

    color="#CCC"
    color_hidden="#000"
    fonts = get_fonts()
    current_font = random.choice(fonts)
    hidden = "VANESSA"
    response = update_graphic(current_font,color,color_hidden,hidden)
    return response

# Variable selection
@app.route('/<font>/<color1>/<color2>/<hidden>')
def update_logo(font,color1,color2,hidden):
    response = update_graphic(font,"#%s" %color1,"#%s" %color2,hidden)
    return response

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
