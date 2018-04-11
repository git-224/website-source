
[TOC]

# Website Project

The idea of this project is to translate the 2/24th site into a series of more human readable pages which can be deligated to and edited by a number of people in 2/24th (allowing for better updates and editing).

These 'somewhat' human readable pages are then built into the website.

So the flow is:

  * Human's edit site: https://github.com/2-24-battalion-org-au/website-source

  * (Some magic process, builds the website)

  * (Technical interest only! The above is used to generate the website repository and is stored at:  https://github.com/2-24-battalion-org-au/2-24-battalion-org-au.github.io . Mostly just ignore this link.)

  * which is browsable at: https://dev-github.battalion.org.au/

## Files in the human readable website

The human readable site is made up of a number of different file types (by their extension):

  * **.md**: markdown is a human like format that makes webpages

  * **.csv**: these files allow data to be extracted from the database and easily converted to html (via **.build** files discussed below)

  * **.build**: for more complex pages (which are made from different bits, eg, markdown and some csv database info) need build instructions which is what this file is

  * **.pdf**, **.jpg**: and a whole lot of other files which are used unchanged for pictures and ff newsletters etc.

## Markdown

You can find details on markdown in a number of places. You can get the general idea from links like this:

  * https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet

Sadly markdown implementations are all sliiiiightly different so some more advanced things might sometimes not work (eg, using a picture as a link). You can still use raw html code but im hoping that wont be much of an issue most of the time.

## Themes

Themes are the 'webcode' wrapped around the content to make it look pretty. (Colors, layout, etc).

Im looking at using some more modern website tools (such as materal-design-light) to make a more modern looking site that has a nice menu at the top and that magically resizes down when used on a phone or tablet.o

Themes are the last thing that you want to do... getting the content right is priority one.


# status of main pages

  * [ ] [photo gallery](gallery.html) -- ON HOLD until i investigate tools for albums in material-design-lite
  * [ ] [battalion rolls](rolls/roll.html)  -- ON HOLD awaiting CSV of rolls (Roland?)

  * [x] [Home](index.html) -- needs theming and to be made pretty like ;-)

  * [x] [the association](association.html)
  * [x] [history of the 2/24th](history.html)
  * [x] [external links](links.html)
  * [x] [contacts](contacts.html)
  * [x] [memorial wall](memwall/memwall.html)
  * [x] [memories](memories.html)
  * [x] [color patches](patches.html)
  * [x] [furphy flyer](fflyer.html)
  * [x] [products](products.html)
  * [x] [committee](committee.html)
  * [x] [reviews](reviews.html)
  * [x] [bibliography](bibliography.html)
  * [x] [lectures and addresses](lecture.html)
  * [x] [search archives](archives.html)
  * [x] [sitemap](sitemap.html)
  * [x] [stories](stories.html)
  * [x] [credits](credits.html)
  * [x] [vale](vale.html)

# Todo...

  * [ ] Get committee to look through site and 'tick off' contents

  * [ ] **product page**:  to refer to contact page for purchases contacts
  * [ ] **product page**:  remove postal address as anyone with a web browser will have email?
  * [ ] **memwall**: fix images?
  * [ ] **memwall**: fix postal address?
  * [ ] **index**: remove rota as association?? make assocations another page?
  * [ ] **index**: Needs much better theme to make it look pretty
  * [ ] **picture gallery**: investigate materal-design-lite image carousels

  * [x] **page**: find all pages  -- DONE and added to 'sitemap' page




