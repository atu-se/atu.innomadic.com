# Introduction

For this exercise, you will need to [download this database file](exercise1.db). It is a database with music data.

1. You should create a folder somewhere on your computer to manage exercises.  Maybe Documents/database_class.  
2. Then for each exercise you can create a separate folder, like exercise2.  
3. Place exercise1.db into the exercise1 folder.  
4. Make a copy of exercise1.db.  Call it *exercise1_original.db*.  Then if you need to refer back to the original database, you will have it readily available.

# 1. Opening an Existing Database

There are two ways to open an existing database.

## A) From the Command Prompt

1. Open your command prompt.
2. Navigate to your *exercise1* folder.  If you've followed my suggestions, you may enter a commands like this:

```shell
$>cd Documents/databases/exercise1
exercise1$>
```

3. When you have successfully reached the folder, do a directory listing.  If you've found the right folder, you should see your new database files, looking something like this:

```shell
exercise1$>            dir
exercise1.db exercise1_original.db
```

4. Now open the database with this command:

```shell
exercise1$>sqlite3 exercise1.db
SQLite version 3.19.3 2017-06-27 16:48:08
Enter ".help" for usage hints.
sqlite>
```

5.  Now you have opened the database!  Enter this command to show you which database you have opened, and its location:

```sqlite
sqlite>.database
```

## B) From within the sqlite shell

You will need to open sqlite in whatever way you prefer  

1. First though, you need to know the complete path to your database file.  I can't tell you exactly what that will be as it depends upon your system setup and folder structures.  Let's use *C:\Users\bob\Documents\exercise1\exercise1.db* for this example.  

2. Now, open sqlite from the Start Menu or from the command prompt.

You should be at the sqlite shell:

```sqlite
sqlite>
```

3. Now enter `.open` followed by your full file path.

```sqlite
sqlite>.open C:\Users\bob\Documents\exercise1\exercise1.db
```

Did it work?

If you did not enter the right path, it will simply create a new database at that location with that name.

Let's check to see if the database opened.  exercise1.db should have 11 tables in it.  

4. List the tables:

```sqlite
sqlite> .tables
albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track
```

If you don't have output like this, then check the path to your database and try step #3 again.  When you successfully list the tables, you're ready to move on to the next step.

# 2 Enter a SQL Query

The moment we've all been waiting for.  Let's enter a SQL query.

```sqlite
sqlite> select * from artists;
```

Did you get a list of artists?  If so, congratulations, you've entered your first SQL query.

Your results should look something like this:




```
%sql select * from artists;
```

    Done.





<table>
    <tr>
        <th>ArtistId</th>
        <th>Name</th>
    </tr>
    <tr>
        <td>1</td>
        <td>AC/DC</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Accept</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Aerosmith</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Alanis Morissette</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Alice In Chains</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Antônio Carlos Jobim</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Apocalyptica</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Audioslave</td>
    </tr>
    <tr>
        <td>9</td>
        <td>BackBeat</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Billy Cobham</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Black Label Society</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Black Sabbath</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Body Count</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Bruce Dickinson</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Buddy Guy</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Caetano Veloso</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Chico Buarque</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Chico Science &amp; Nação Zumbi</td>
    </tr>
    <tr>
        <td>19</td>
        <td>Cidade Negra</td>
    </tr>
    <tr>
        <td>20</td>
        <td>Cláudio Zoli</td>
    </tr>
    <tr>
        <td>21</td>
        <td>Various Artists</td>
    </tr>
    <tr>
        <td>22</td>
        <td>Led Zeppelin</td>
    </tr>
    <tr>
        <td>23</td>
        <td>Frank Zappa &amp; Captain Beefheart</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Marcos Valle</td>
    </tr>
    <tr>
        <td>25</td>
        <td>Milton Nascimento &amp; Bebeto</td>
    </tr>
    <tr>
        <td>26</td>
        <td>Azymuth</td>
    </tr>
    <tr>
        <td>27</td>
        <td>Gilberto Gil</td>
    </tr>
    <tr>
        <td>28</td>
        <td>João Gilberto</td>
    </tr>
    <tr>
        <td>29</td>
        <td>Bebel Gilberto</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Jorge Vercilo</td>
    </tr>
    <tr>
        <td>31</td>
        <td>Baby Consuelo</td>
    </tr>
    <tr>
        <td>32</td>
        <td>Ney Matogrosso</td>
    </tr>
    <tr>
        <td>33</td>
        <td>Luiz Melodia</td>
    </tr>
    <tr>
        <td>34</td>
        <td>Nando Reis</td>
    </tr>
    <tr>
        <td>35</td>
        <td>Pedro Luís &amp; A Parede</td>
    </tr>
    <tr>
        <td>36</td>
        <td>O Rappa</td>
    </tr>
    <tr>
        <td>37</td>
        <td>Ed Motta</td>
    </tr>
    <tr>
        <td>38</td>
        <td>Banda Black Rio</td>
    </tr>
    <tr>
        <td>39</td>
        <td>Fernanda Porto</td>
    </tr>
    <tr>
        <td>40</td>
        <td>Os Cariocas</td>
    </tr>
    <tr>
        <td>41</td>
        <td>Elis Regina</td>
    </tr>
    <tr>
        <td>42</td>
        <td>Milton Nascimento</td>
    </tr>
    <tr>
        <td>43</td>
        <td>A Cor Do Som</td>
    </tr>
    <tr>
        <td>44</td>
        <td>Kid Abelha</td>
    </tr>
    <tr>
        <td>45</td>
        <td>Sandra De Sá</td>
    </tr>
    <tr>
        <td>46</td>
        <td>Jorge Ben</td>
    </tr>
    <tr>
        <td>47</td>
        <td>Hermeto Pascoal</td>
    </tr>
    <tr>
        <td>48</td>
        <td>Barão Vermelho</td>
    </tr>
    <tr>
        <td>49</td>
        <td>Edson, DJ Marky &amp; DJ Patife Featuring Fernanda Porto</td>
    </tr>
    <tr>
        <td>50</td>
        <td>Metallica</td>
    </tr>
    <tr>
        <td>51</td>
        <td>Queen</td>
    </tr>
    <tr>
        <td>52</td>
        <td>Kiss</td>
    </tr>
    <tr>
        <td>53</td>
        <td>Spyro Gyra</td>
    </tr>
    <tr>
        <td>54</td>
        <td>Green Day</td>
    </tr>
    <tr>
        <td>55</td>
        <td>David Coverdale</td>
    </tr>
    <tr>
        <td>56</td>
        <td>Gonzaguinha</td>
    </tr>
    <tr>
        <td>57</td>
        <td>Os Mutantes</td>
    </tr>
    <tr>
        <td>58</td>
        <td>Deep Purple</td>
    </tr>
    <tr>
        <td>59</td>
        <td>Santana</td>
    </tr>
    <tr>
        <td>60</td>
        <td>Santana Feat. Dave Matthews</td>
    </tr>
    <tr>
        <td>61</td>
        <td>Santana Feat. Everlast</td>
    </tr>
    <tr>
        <td>62</td>
        <td>Santana Feat. Rob Thomas</td>
    </tr>
    <tr>
        <td>63</td>
        <td>Santana Feat. Lauryn Hill &amp; Cee-Lo</td>
    </tr>
    <tr>
        <td>64</td>
        <td>Santana Feat. The Project G&amp;B</td>
    </tr>
    <tr>
        <td>65</td>
        <td>Santana Feat. Maná</td>
    </tr>
    <tr>
        <td>66</td>
        <td>Santana Feat. Eagle-Eye Cherry</td>
    </tr>
    <tr>
        <td>67</td>
        <td>Santana Feat. Eric Clapton</td>
    </tr>
    <tr>
        <td>68</td>
        <td>Miles Davis</td>
    </tr>
    <tr>
        <td>69</td>
        <td>Gene Krupa</td>
    </tr>
    <tr>
        <td>70</td>
        <td>Toquinho &amp; Vinícius</td>
    </tr>
    <tr>
        <td>71</td>
        <td>Vinícius De Moraes &amp; Baden Powell</td>
    </tr>
    <tr>
        <td>72</td>
        <td>Vinícius De Moraes</td>
    </tr>
    <tr>
        <td>73</td>
        <td>Vinícius E Qurteto Em Cy</td>
    </tr>
    <tr>
        <td>74</td>
        <td>Vinícius E Odette Lara</td>
    </tr>
    <tr>
        <td>75</td>
        <td>Vinicius, Toquinho &amp; Quarteto Em Cy</td>
    </tr>
    <tr>
        <td>76</td>
        <td>Creedence Clearwater Revival</td>
    </tr>
    <tr>
        <td>77</td>
        <td>Cássia Eller</td>
    </tr>
    <tr>
        <td>78</td>
        <td>Def Leppard</td>
    </tr>
    <tr>
        <td>79</td>
        <td>Dennis Chambers</td>
    </tr>
    <tr>
        <td>80</td>
        <td>Djavan</td>
    </tr>
    <tr>
        <td>81</td>
        <td>Eric Clapton</td>
    </tr>
    <tr>
        <td>82</td>
        <td>Faith No More</td>
    </tr>
    <tr>
        <td>83</td>
        <td>Falamansa</td>
    </tr>
    <tr>
        <td>84</td>
        <td>Foo Fighters</td>
    </tr>
    <tr>
        <td>85</td>
        <td>Frank Sinatra</td>
    </tr>
    <tr>
        <td>86</td>
        <td>Funk Como Le Gusta</td>
    </tr>
    <tr>
        <td>87</td>
        <td>Godsmack</td>
    </tr>
    <tr>
        <td>88</td>
        <td>Guns N&#x27; Roses</td>
    </tr>
    <tr>
        <td>89</td>
        <td>Incognito</td>
    </tr>
    <tr>
        <td>90</td>
        <td>Iron Maiden</td>
    </tr>
    <tr>
        <td>91</td>
        <td>James Brown</td>
    </tr>
    <tr>
        <td>92</td>
        <td>Jamiroquai</td>
    </tr>
    <tr>
        <td>93</td>
        <td>JET</td>
    </tr>
    <tr>
        <td>94</td>
        <td>Jimi Hendrix</td>
    </tr>
    <tr>
        <td>95</td>
        <td>Joe Satriani</td>
    </tr>
    <tr>
        <td>96</td>
        <td>Jota Quest</td>
    </tr>
    <tr>
        <td>97</td>
        <td>João Suplicy</td>
    </tr>
    <tr>
        <td>98</td>
        <td>Judas Priest</td>
    </tr>
    <tr>
        <td>99</td>
        <td>Legião Urbana</td>
    </tr>
    <tr>
        <td>100</td>
        <td>Lenny Kravitz</td>
    </tr>
    <tr>
        <td>101</td>
        <td>Lulu Santos</td>
    </tr>
    <tr>
        <td>102</td>
        <td>Marillion</td>
    </tr>
    <tr>
        <td>103</td>
        <td>Marisa Monte</td>
    </tr>
    <tr>
        <td>104</td>
        <td>Marvin Gaye</td>
    </tr>
    <tr>
        <td>105</td>
        <td>Men At Work</td>
    </tr>
    <tr>
        <td>106</td>
        <td>Motörhead</td>
    </tr>
    <tr>
        <td>107</td>
        <td>Motörhead &amp; Girlschool</td>
    </tr>
    <tr>
        <td>108</td>
        <td>Mônica Marianno</td>
    </tr>
    <tr>
        <td>109</td>
        <td>Mötley Crüe</td>
    </tr>
    <tr>
        <td>110</td>
        <td>Nirvana</td>
    </tr>
    <tr>
        <td>111</td>
        <td>O Terço</td>
    </tr>
    <tr>
        <td>112</td>
        <td>Olodum</td>
    </tr>
    <tr>
        <td>113</td>
        <td>Os Paralamas Do Sucesso</td>
    </tr>
    <tr>
        <td>114</td>
        <td>Ozzy Osbourne</td>
    </tr>
    <tr>
        <td>115</td>
        <td>Page &amp; Plant</td>
    </tr>
    <tr>
        <td>116</td>
        <td>Passengers</td>
    </tr>
    <tr>
        <td>117</td>
        <td>Paul D&#x27;Ianno</td>
    </tr>
    <tr>
        <td>118</td>
        <td>Pearl Jam</td>
    </tr>
    <tr>
        <td>119</td>
        <td>Peter Tosh</td>
    </tr>
    <tr>
        <td>120</td>
        <td>Pink Floyd</td>
    </tr>
    <tr>
        <td>121</td>
        <td>Planet Hemp</td>
    </tr>
    <tr>
        <td>122</td>
        <td>R.E.M. Feat. Kate Pearson</td>
    </tr>
    <tr>
        <td>123</td>
        <td>R.E.M. Feat. KRS-One</td>
    </tr>
    <tr>
        <td>124</td>
        <td>R.E.M.</td>
    </tr>
    <tr>
        <td>125</td>
        <td>Raimundos</td>
    </tr>
    <tr>
        <td>126</td>
        <td>Raul Seixas</td>
    </tr>
    <tr>
        <td>127</td>
        <td>Red Hot Chili Peppers</td>
    </tr>
    <tr>
        <td>128</td>
        <td>Rush</td>
    </tr>
    <tr>
        <td>129</td>
        <td>Simply Red</td>
    </tr>
    <tr>
        <td>130</td>
        <td>Skank</td>
    </tr>
    <tr>
        <td>131</td>
        <td>Smashing Pumpkins</td>
    </tr>
    <tr>
        <td>132</td>
        <td>Soundgarden</td>
    </tr>
    <tr>
        <td>133</td>
        <td>Stevie Ray Vaughan &amp; Double Trouble</td>
    </tr>
    <tr>
        <td>134</td>
        <td>Stone Temple Pilots</td>
    </tr>
    <tr>
        <td>135</td>
        <td>System Of A Down</td>
    </tr>
    <tr>
        <td>136</td>
        <td>Terry Bozzio, Tony Levin &amp; Steve Stevens</td>
    </tr>
    <tr>
        <td>137</td>
        <td>The Black Crowes</td>
    </tr>
    <tr>
        <td>138</td>
        <td>The Clash</td>
    </tr>
    <tr>
        <td>139</td>
        <td>The Cult</td>
    </tr>
    <tr>
        <td>140</td>
        <td>The Doors</td>
    </tr>
    <tr>
        <td>141</td>
        <td>The Police</td>
    </tr>
    <tr>
        <td>142</td>
        <td>The Rolling Stones</td>
    </tr>
    <tr>
        <td>143</td>
        <td>The Tea Party</td>
    </tr>
    <tr>
        <td>144</td>
        <td>The Who</td>
    </tr>
    <tr>
        <td>145</td>
        <td>Tim Maia</td>
    </tr>
    <tr>
        <td>146</td>
        <td>Titãs</td>
    </tr>
    <tr>
        <td>147</td>
        <td>Battlestar Galactica</td>
    </tr>
    <tr>
        <td>148</td>
        <td>Heroes</td>
    </tr>
    <tr>
        <td>149</td>
        <td>Lost</td>
    </tr>
    <tr>
        <td>150</td>
        <td>U2</td>
    </tr>
    <tr>
        <td>151</td>
        <td>UB40</td>
    </tr>
    <tr>
        <td>152</td>
        <td>Van Halen</td>
    </tr>
    <tr>
        <td>153</td>
        <td>Velvet Revolver</td>
    </tr>
    <tr>
        <td>154</td>
        <td>Whitesnake</td>
    </tr>
    <tr>
        <td>155</td>
        <td>Zeca Pagodinho</td>
    </tr>
    <tr>
        <td>156</td>
        <td>The Office</td>
    </tr>
    <tr>
        <td>157</td>
        <td>Dread Zeppelin</td>
    </tr>
    <tr>
        <td>158</td>
        <td>Battlestar Galactica (Classic)</td>
    </tr>
    <tr>
        <td>159</td>
        <td>Aquaman</td>
    </tr>
    <tr>
        <td>160</td>
        <td>Christina Aguilera featuring BigElf</td>
    </tr>
    <tr>
        <td>161</td>
        <td>Aerosmith &amp; Sierra Leone&#x27;s Refugee Allstars</td>
    </tr>
    <tr>
        <td>162</td>
        <td>Los Lonely Boys</td>
    </tr>
    <tr>
        <td>163</td>
        <td>Corinne Bailey Rae</td>
    </tr>
    <tr>
        <td>164</td>
        <td>Dhani Harrison &amp; Jakob Dylan</td>
    </tr>
    <tr>
        <td>165</td>
        <td>Jackson Browne</td>
    </tr>
    <tr>
        <td>166</td>
        <td>Avril Lavigne</td>
    </tr>
    <tr>
        <td>167</td>
        <td>Big &amp; Rich</td>
    </tr>
    <tr>
        <td>168</td>
        <td>Youssou N&#x27;Dour</td>
    </tr>
    <tr>
        <td>169</td>
        <td>Black Eyed Peas</td>
    </tr>
    <tr>
        <td>170</td>
        <td>Jack Johnson</td>
    </tr>
    <tr>
        <td>171</td>
        <td>Ben Harper</td>
    </tr>
    <tr>
        <td>172</td>
        <td>Snow Patrol</td>
    </tr>
    <tr>
        <td>173</td>
        <td>Matisyahu</td>
    </tr>
    <tr>
        <td>174</td>
        <td>The Postal Service</td>
    </tr>
    <tr>
        <td>175</td>
        <td>Jaguares</td>
    </tr>
    <tr>
        <td>176</td>
        <td>The Flaming Lips</td>
    </tr>
    <tr>
        <td>177</td>
        <td>Jack&#x27;s Mannequin &amp; Mick Fleetwood</td>
    </tr>
    <tr>
        <td>178</td>
        <td>Regina Spektor</td>
    </tr>
    <tr>
        <td>179</td>
        <td>Scorpions</td>
    </tr>
    <tr>
        <td>180</td>
        <td>House Of Pain</td>
    </tr>
    <tr>
        <td>181</td>
        <td>Xis</td>
    </tr>
    <tr>
        <td>182</td>
        <td>Nega Gizza</td>
    </tr>
    <tr>
        <td>183</td>
        <td>Gustavo &amp; Andres Veiga &amp; Salazar</td>
    </tr>
    <tr>
        <td>184</td>
        <td>Rodox</td>
    </tr>
    <tr>
        <td>185</td>
        <td>Charlie Brown Jr.</td>
    </tr>
    <tr>
        <td>186</td>
        <td>Pedro Luís E A Parede</td>
    </tr>
    <tr>
        <td>187</td>
        <td>Los Hermanos</td>
    </tr>
    <tr>
        <td>188</td>
        <td>Mundo Livre S/A</td>
    </tr>
    <tr>
        <td>189</td>
        <td>Otto</td>
    </tr>
    <tr>
        <td>190</td>
        <td>Instituto</td>
    </tr>
    <tr>
        <td>191</td>
        <td>Nação Zumbi</td>
    </tr>
    <tr>
        <td>192</td>
        <td>DJ Dolores &amp; Orchestra Santa Massa</td>
    </tr>
    <tr>
        <td>193</td>
        <td>Seu Jorge</td>
    </tr>
    <tr>
        <td>194</td>
        <td>Sabotage E Instituto</td>
    </tr>
    <tr>
        <td>195</td>
        <td>Stereo Maracana</td>
    </tr>
    <tr>
        <td>196</td>
        <td>Cake</td>
    </tr>
    <tr>
        <td>197</td>
        <td>Aisha Duo</td>
    </tr>
    <tr>
        <td>198</td>
        <td>Habib Koité and Bamada</td>
    </tr>
    <tr>
        <td>199</td>
        <td>Karsh Kale</td>
    </tr>
    <tr>
        <td>200</td>
        <td>The Posies</td>
    </tr>
    <tr>
        <td>201</td>
        <td>Luciana Souza/Romero Lubambo</td>
    </tr>
    <tr>
        <td>202</td>
        <td>Aaron Goldberg</td>
    </tr>
    <tr>
        <td>203</td>
        <td>Nicolaus Esterhazy Sinfonia</td>
    </tr>
    <tr>
        <td>204</td>
        <td>Temple of the Dog</td>
    </tr>
    <tr>
        <td>205</td>
        <td>Chris Cornell</td>
    </tr>
    <tr>
        <td>206</td>
        <td>Alberto Turco &amp; Nova Schola Gregoriana</td>
    </tr>
    <tr>
        <td>207</td>
        <td>Richard Marlow &amp; The Choir of Trinity College, Cambridge</td>
    </tr>
    <tr>
        <td>208</td>
        <td>English Concert &amp; Trevor Pinnock</td>
    </tr>
    <tr>
        <td>209</td>
        <td>Anne-Sophie Mutter, Herbert Von Karajan &amp; Wiener Philharmoniker</td>
    </tr>
    <tr>
        <td>210</td>
        <td>Hilary Hahn, Jeffrey Kahane, Los Angeles Chamber Orchestra &amp; Margaret Batjer</td>
    </tr>
    <tr>
        <td>211</td>
        <td>Wilhelm Kempff</td>
    </tr>
    <tr>
        <td>212</td>
        <td>Yo-Yo Ma</td>
    </tr>
    <tr>
        <td>213</td>
        <td>Scholars Baroque Ensemble</td>
    </tr>
    <tr>
        <td>214</td>
        <td>Academy of St. Martin in the Fields &amp; Sir Neville Marriner</td>
    </tr>
    <tr>
        <td>215</td>
        <td>Academy of St. Martin in the Fields Chamber Ensemble &amp; Sir Neville Marriner</td>
    </tr>
    <tr>
        <td>216</td>
        <td>Berliner Philharmoniker, Claudio Abbado &amp; Sabine Meyer</td>
    </tr>
    <tr>
        <td>217</td>
        <td>Royal Philharmonic Orchestra &amp; Sir Thomas Beecham</td>
    </tr>
    <tr>
        <td>218</td>
        <td>Orchestre Révolutionnaire et Romantique &amp; John Eliot Gardiner</td>
    </tr>
    <tr>
        <td>219</td>
        <td>Britten Sinfonia, Ivor Bolton &amp; Lesley Garrett</td>
    </tr>
    <tr>
        <td>220</td>
        <td>Chicago Symphony Chorus, Chicago Symphony Orchestra &amp; Sir Georg Solti</td>
    </tr>
    <tr>
        <td>221</td>
        <td>Sir Georg Solti &amp; Wiener Philharmoniker</td>
    </tr>
    <tr>
        <td>222</td>
        <td>Academy of St. Martin in the Fields, John Birch, Sir Neville Marriner &amp; Sylvia McNair</td>
    </tr>
    <tr>
        <td>223</td>
        <td>London Symphony Orchestra &amp; Sir Charles Mackerras</td>
    </tr>
    <tr>
        <td>224</td>
        <td>Barry Wordsworth &amp; BBC Concert Orchestra</td>
    </tr>
    <tr>
        <td>225</td>
        <td>Herbert Von Karajan, Mirella Freni &amp; Wiener Philharmoniker</td>
    </tr>
    <tr>
        <td>226</td>
        <td>Eugene Ormandy</td>
    </tr>
    <tr>
        <td>227</td>
        <td>Luciano Pavarotti</td>
    </tr>
    <tr>
        <td>228</td>
        <td>Leonard Bernstein &amp; New York Philharmonic</td>
    </tr>
    <tr>
        <td>229</td>
        <td>Boston Symphony Orchestra &amp; Seiji Ozawa</td>
    </tr>
    <tr>
        <td>230</td>
        <td>Aaron Copland &amp; London Symphony Orchestra</td>
    </tr>
    <tr>
        <td>231</td>
        <td>Ton Koopman</td>
    </tr>
    <tr>
        <td>232</td>
        <td>Sergei Prokofiev &amp; Yuri Temirkanov</td>
    </tr>
    <tr>
        <td>233</td>
        <td>Chicago Symphony Orchestra &amp; Fritz Reiner</td>
    </tr>
    <tr>
        <td>234</td>
        <td>Orchestra of The Age of Enlightenment</td>
    </tr>
    <tr>
        <td>235</td>
        <td>Emanuel Ax, Eugene Ormandy &amp; Philadelphia Orchestra</td>
    </tr>
    <tr>
        <td>236</td>
        <td>James Levine</td>
    </tr>
    <tr>
        <td>237</td>
        <td>Berliner Philharmoniker &amp; Hans Rosbaud</td>
    </tr>
    <tr>
        <td>238</td>
        <td>Maurizio Pollini</td>
    </tr>
    <tr>
        <td>239</td>
        <td>Academy of St. Martin in the Fields, Sir Neville Marriner &amp; William Bennett</td>
    </tr>
    <tr>
        <td>240</td>
        <td>Gustav Mahler</td>
    </tr>
    <tr>
        <td>241</td>
        <td>Felix Schmidt, London Symphony Orchestra &amp; Rafael Frühbeck de Burgos</td>
    </tr>
    <tr>
        <td>242</td>
        <td>Edo de Waart &amp; San Francisco Symphony</td>
    </tr>
    <tr>
        <td>243</td>
        <td>Antal Doráti &amp; London Symphony Orchestra</td>
    </tr>
    <tr>
        <td>244</td>
        <td>Choir Of Westminster Abbey &amp; Simon Preston</td>
    </tr>
    <tr>
        <td>245</td>
        <td>Michael Tilson Thomas &amp; San Francisco Symphony</td>
    </tr>
    <tr>
        <td>246</td>
        <td>Chor der Wiener Staatsoper, Herbert Von Karajan &amp; Wiener Philharmoniker</td>
    </tr>
    <tr>
        <td>247</td>
        <td>The King&#x27;s Singers</td>
    </tr>
    <tr>
        <td>248</td>
        <td>Berliner Philharmoniker &amp; Herbert Von Karajan</td>
    </tr>
    <tr>
        <td>249</td>
        <td>Sir Georg Solti, Sumi Jo &amp; Wiener Philharmoniker</td>
    </tr>
    <tr>
        <td>250</td>
        <td>Christopher O&#x27;Riley</td>
    </tr>
    <tr>
        <td>251</td>
        <td>Fretwork</td>
    </tr>
    <tr>
        <td>252</td>
        <td>Amy Winehouse</td>
    </tr>
    <tr>
        <td>253</td>
        <td>Calexico</td>
    </tr>
    <tr>
        <td>254</td>
        <td>Otto Klemperer &amp; Philharmonia Orchestra</td>
    </tr>
    <tr>
        <td>255</td>
        <td>Yehudi Menuhin</td>
    </tr>
    <tr>
        <td>256</td>
        <td>Philharmonia Orchestra &amp; Sir Neville Marriner</td>
    </tr>
    <tr>
        <td>257</td>
        <td>Academy of St. Martin in the Fields, Sir Neville Marriner &amp; Thurston Dart</td>
    </tr>
    <tr>
        <td>258</td>
        <td>Les Arts Florissants &amp; William Christie</td>
    </tr>
    <tr>
        <td>259</td>
        <td>The 12 Cellists of The Berlin Philharmonic</td>
    </tr>
    <tr>
        <td>260</td>
        <td>Adrian Leaper &amp; Doreen de Feis</td>
    </tr>
    <tr>
        <td>261</td>
        <td>Roger Norrington, London Classical Players</td>
    </tr>
    <tr>
        <td>262</td>
        <td>Charles Dutoit &amp; L&#x27;Orchestre Symphonique de Montréal</td>
    </tr>
    <tr>
        <td>263</td>
        <td>Equale Brass Ensemble, John Eliot Gardiner &amp; Munich Monteverdi Orchestra and Choir</td>
    </tr>
    <tr>
        <td>264</td>
        <td>Kent Nagano and Orchestre de l&#x27;Opéra de Lyon</td>
    </tr>
    <tr>
        <td>265</td>
        <td>Julian Bream</td>
    </tr>
    <tr>
        <td>266</td>
        <td>Martin Roscoe</td>
    </tr>
    <tr>
        <td>267</td>
        <td>Göteborgs Symfoniker &amp; Neeme Järvi</td>
    </tr>
    <tr>
        <td>268</td>
        <td>Itzhak Perlman</td>
    </tr>
    <tr>
        <td>269</td>
        <td>Michele Campanella</td>
    </tr>
    <tr>
        <td>270</td>
        <td>Gerald Moore</td>
    </tr>
    <tr>
        <td>271</td>
        <td>Mela Tenenbaum, Pro Musica Prague &amp; Richard Kapp</td>
    </tr>
    <tr>
        <td>272</td>
        <td>Emerson String Quartet</td>
    </tr>
    <tr>
        <td>273</td>
        <td>C. Monteverdi, Nigel Rogers - Chiaroscuro; London Baroque; London Cornett &amp; Sackbu</td>
    </tr>
    <tr>
        <td>274</td>
        <td>Nash Ensemble</td>
    </tr>
    <tr>
        <td>275</td>
        <td>Philip Glass Ensemble</td>
    </tr>
</table>

When you've completed this, move on to [Exercise 1c](exercise1c).
