from bs4 import BeautifulSoup
import re
import requests
import json
html="""
<div class="promoted-listings"></div>	<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie Centrale AngrÃ©" data-postid="9896"   data-lattitue="5.41248334402694" data-longitute="-3.9828121662139893" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-centrale-angre/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9896" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-centrale-angre/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie Centrale AngrÃ©"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-centrale-angre/">Pharmacie Centrale AngrÃ© </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/angre-chateau/">AngrÃ© ChÃ¢teau, Cocody</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 22 46 74 25" class="grind-number">+225 22 46 74 25</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9896" data-lat="5.41248334402694" data-lng="-3.9828121662139893" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9896" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-centrale-angre/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie Centrale AngrÃ©"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-centrale-angre/">Pharmacie Centrale AngrÃ© </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Abidjan, Cocody, Blvd Latrille, rez de chaussÃ©e de l'immeuble Abri 2000, a 100m du chateau d'eau</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 22 46 74 25" class="grind-number">+225 22 46 74 25</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9896" data-lat="5.41248334402694" data-lng="-3.9828121662139893" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵					<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie bonne fortune" data-postid="9611"   data-lattitue="5.335270384204668" data-longitute="-3.9393055628567026" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-bonne-fortune/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9611" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-bonne-fortune/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie bonne fortune"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-bonne-fortune/">Pharmacie bonne fortune </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/mbadon/">Riviera MâBadon, Cocody</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 22 46 76 42" class="grind-number">+225 22 46 76 42</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9611" data-lat="5.335270384204668" data-lng="-3.9393055628567026" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9611" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-bonne-fortune/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie bonne fortune"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-bonne-fortune/">Pharmacie bonne fortune </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Abidjan, Cocody, Riviera M'Badon, Route de l'UniversitÃ© UIPA avant le centre de santÃ© communautaire de m'Badon</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 22 46 76 42" class="grind-number">+225 22 46 76 42</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9611" data-lat="5.335270384204668" data-lng="-3.9393055628567026" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵				<div class="clearfix"></div>	<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie de la Mairie" data-postid="9413"   data-lattitue="5.4197878" data-longitute="-4.015565" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-de-la-mairie-yopougon/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9413" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-de-la-mairie-yopougon/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2019/01/Pharmacie-de-la-Mairie-372x240.jpg" alt="Pharmacie de la Mairie"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-de-la-mairie-yopougon/">Pharmacie de la Mairie </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/selmer/">Selmer, Yopougon</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 23 52 43 06" class="grind-number">+225 23 52 43 06</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9413" data-lat="5.4197878" data-lng="-4.015565" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9413" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-de-la-mairie-yopougon/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2019/01/Pharmacie-de-la-Mairie-272x231.jpg" alt="Pharmacie de la Mairie"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-de-la-mairie-yopougon/">Pharmacie de la Mairie </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Abidjan Yopougon Selmer, Ã  200 de la mairie face maquis tantie Margot ligne bus 30</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 23 52 43 06" class="grind-number">+225 23 52 43 06</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9413" data-lat="5.4197878" data-lng="-4.015565" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵					<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie du grand marchÃ©" data-postid="9388"   data-lattitue="" data-longitute="" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-grand-marche/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9388" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-grand-marche/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie du grand marchÃ©"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-grand-marche/">Pharmacie du grand marchÃ... </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/treichville/">Treichville</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 21 24 00 72" class="grind-number">+225 21 24 00 72</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9388" data-lat="" data-lng="" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9388" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-grand-marche/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie du grand marchÃ©"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-grand-marche/">Pharmacie du grand marchÃ© </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Treichville</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 21 24 00 72" class="grind-number">+225 21 24 00 72</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9388" data-lat="" data-lng="" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵				<div class="clearfix"></div>	<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie des Lagunes" data-postid="9271"   data-lattitue="0" data-longitute="0" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-des-lagunes-marcory/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9271" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-des-lagunes-marcory/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie des Lagunes"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-des-lagunes-marcory/">Pharmacie des Lagunes </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/marcory/">Marcory</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 21 26 12 40" class="grind-number">+225 21 26 12 40</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9271" data-lat="0" data-lng="0" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9271" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-des-lagunes-marcory/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie des Lagunes"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-des-lagunes-marcory/">Pharmacie des Lagunes </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Marcory</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 21 26 12 40" class="grind-number">+225 21 26 12 40</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9271" data-lat="0" data-lng="0" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵					<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie lycÃ©e club" data-postid="9257"   data-lattitue="" data-longitute="" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-lycee-club/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9257" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-lycee-club/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie lycÃ©e club"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-lycee-club/">Pharmacie lycÃ©e club </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/man/">Man</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 01 00 61 24" class="grind-number">+225 01 00 61 24</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9257" data-lat="" data-lng="" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9257" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-lycee-club/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie lycÃ©e club"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-lycee-club/">Pharmacie lycÃ©e club </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Man, quartier lycÃ©e rÃ©sidentiel</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 01 00 61 24" class="grind-number">+225 01 00 61 24</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9257" data-lat="" data-lng="" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵				<div class="clearfix"></div>	<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie moderne" data-postid="9253"   data-lattitue="" data-longitute="" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-moderne-man/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9253" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-moderne-man/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie moderne"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-moderne-man/">Pharmacie moderne </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/man/">Man</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 33 79 03 39" class="grind-number">+225 33 79 03 39</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9253" data-lat="" data-lng="" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9253" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-moderne-man/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie moderne"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-moderne-man/">Pharmacie moderne </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Man</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 33 79 03 39" class="grind-number">+225 33 79 03 39</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9253" data-lat="" data-lng="" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵					<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie Notre Dame" data-postid="9004"   data-lattitue="9.480440998952817" data-longitute="-5.641487036230956" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-notre-dame-korhogo/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9004" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-notre-dame-korhogo/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie Notre Dame"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-notre-dame-korhogo/">Pharmacie Notre Dame </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/korhogo/">Korhogo</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 08 61 42 61" class="grind-number">+225 08 61 42 61</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9004" data-lat="9.480440998952817" data-lng="-5.641487036230956" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9004" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-notre-dame-korhogo/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie Notre Dame"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-notre-dame-korhogo/">Pharmacie Notre Dame </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Korhogo</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 08 61 42 61" class="grind-number">+225 08 61 42 61</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9004" data-lat="9.480440998952817" data-lng="-5.641487036230956" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵				<div class="clearfix"></div>	<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie Nour" data-postid="9003"   data-lattitue="9.457654235284924" data-longitute="-5.630948301735316" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-nour-korhogo/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9003" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-nour-korhogo/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie Nour"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-nour-korhogo/">Pharmacie Nour </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/korhogo/">Korhogo</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 36 86 07 39" class="grind-number">+225 36 86 07 39</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9003" data-lat="9.457654235284924" data-lng="-5.630948301735316" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9003" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-nour-korhogo/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie Nour"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-nour-korhogo/">Pharmacie Nour </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Korhogo</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 36 86 07 39" class="grind-number">+225 36 86 07 39</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9003" data-lat="9.457654235284924" data-lng="-5.630948301735316" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵					<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class lp-grid-box-contianer" data-title="Pharmacie du nord" data-postid="9002"   data-lattitue="9.45731028753612" data-longitute="-5.629446264686976" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-du-nord/">
↵    <div class="lp-listing">
↵        <div class="grid-style-container">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9002" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵               
↵                <div class="clearfix lp-listing-discount-outer">
↵
↵                                       
↵                </div>
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-du-nord/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie du nord"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                           <div class="clearfix"></div>
↵                <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-du-nord/">Pharmacie du nord </a></h4>
↵                <div class="lp-listing-cats">
↵                    <a href=""></a>
↵                </div>
↵
↵                <div class="lp-listing-stars">
↵                    
↵                        <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                        
↵                </div>
↵                <div class="lp-listing-location"><i class="fa fa-map-marker" aria-hidden="true"></i> <a href="http://www.pagesjaunes.ci/location/korhogo/">Korhogo</a></div>                <div class="clearfix"></div>
↵            </div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 36 86 02 74" class="grind-number">+225 36 86 02 74</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9002" data-lat="9.45731028753612" data-lng="-5.629446264686976" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵        <div class="list-style-cotainer">
↵            <div class="lp-listing-top">
↵                <a href="#" data-post-id="9002" data-post-type="list" class="lp-listing-favrt add-to-fav-v2">
↵                    <i class="fa fa-heart-o" aria-hidden="true"></i>
↵                </a>
↵
↵
↵                <div class="lp-listing-top-thumb">
↵                    <a href="http://www.pagesjaunes.ci/item/pharmacie-du-nord/"><img src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/annuaire.jpg" alt="Pharmacie du nord"></a>
↵                </div>
↵            </div>
↵            <div class="lp-listing-bottom">
↵                <div class="0 clearfix lp-listing-bottom-left-full ">
↵                    <span class="cat-icon" style="display:none;"><img class="icon icons8-Food" src="http://www.pagesjaunes.ci/wp-content/uploads/2017/01/pharmacie-300x300.png" alt="cat-icon"></span>                                    <a href="http://www.pagesjaunes.ci/categorie/pharmacies/" class="lp-listing-cat">Pharmacies</a>
↵                                                                                                                                                     <div class="clearfix"></div>
↵                    <div class="lp-bottom-left-full-outer">
↵                        <h4> <a href="http://www.pagesjaunes.ci/item/pharmacie-du-nord/">Pharmacie du nord </a></h4>
↵
↵                                                <div class="lp-listing-stars">
↵                            
↵                                <span class="lp-ann-btn lp-no-review-btn">Soyez le premier Ã  laisser un avis !</span>
↵
↵                                
↵                        </div>
↵                        <div class="clearfix"></div>
↵                                                <div class="clearfix">
↵                                                                                </div>
↵                                                    <div class="lp-listing-location">
↵								<p class="margin-bottom-0"><i class="fa fa-map-marker" aria-hidden="true"></i> Korhogo</p>
↵							</div>
↵                        
↵                        <div class="clearfix"></div>
↵
↵                    </div>
↵                                    </div>
↵
↵                <div class="clearfix"></div>
↵            </div>
↵
↵            <div class="clearfix"></div>
↵                            <div class="lp-new-grid-bottom-button">
↵                    <ul class="clearfix">
↵
↵                                                    <li class="show-number-wrap" style="">
↵                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span class="show-number">Appeler</span><a href="tel:+225 36 86 02 74" class="grind-number">+225 36 86 02 74</a></p>
↵                            </li>
↵                                                                            <li style="">
↵                                <a href="" data-lid="9002" data-lat="9.45731028753612" data-lng="-5.629446264686976" class="show-loop-map-popup"><i class="fa fa-map-pin" aria-hidden="true"></i> Afficher la carte</a>
↵                            </li>
↵                                                                    </ul>
↵                </div>
↵                    </div>
↵    </div>
↵</div>
↵													 
↵				<div class="clearfix"></div><div class="lp-pagination pagination lp-filter-pagination-ajx"><ul class="page-numbers"><li><span data-pageurl="1"  class="page-numbers  haspaglink current">1</span></li></li><li><span data-pageurl="2"  class="page-numbers haspaglink">2</span></li></li><li><span data-pageurl="3"  class="page-numbers haspaglink">3</span></li></li><li><span data-pageurl="4"  class="page-numbers haspaglink">4</span></li></li><li><span data-pageurl="5"  class="page-numbers haspaglink">5</span></li></li><li><span data-pageurl="6"  class="page-numbers haspaglink">6</span></li></li></li></li></li></li></li></li></li></li></ul></div>
"""
div_sui=[]
pattern = re.compile("")
soup = BeautifulSoup(html,'html.parser')
div = soup.find_all('a')
for d in div:
    if re.match('http://www\.pagesjaunes\.ci/item/pharmacie-[a-zA-Z0-9\-]*/?',d['href'])  and re.match('^(Pharmacie)',str(d.contents[0])) :
        print('\r\n====================================================\r\n',d,'\r\n==================================================\r\n')
        print('\r\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\r\n',d.contents[0],'\r\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\r\n')
