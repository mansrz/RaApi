Espol Ra


Api


Models: 
  Places
    Type of places, example: 'Administrativo'

  Position:
    Point have a lat, long, name and relation with one Place(table)

urls : 
  /admin/
  /places/
  /position
  /map
  /

  /:
    Login

  Map:
    Template with google maps api, can select point to save a position and filter. (Only visible for user authenticated)
    Template with google maps api for user not authenticated can filter positions and see path from actual direction

  Places: 
    Get a list of places 

  Position:
    Get a list of positions
    Send parameter (?type=N) in GET method, filter for place 
    Post a position
