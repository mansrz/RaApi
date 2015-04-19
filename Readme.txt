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

  Places: 
    Get a list of places 

  Position:
    Get a list of positions
    Send parameter (?type=N) in GET method, filter for place 
