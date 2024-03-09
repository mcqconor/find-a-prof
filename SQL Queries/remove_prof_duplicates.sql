DELETE p FROM professors p
  INNER JOIN professors p2
WHERE p.id < p2.id
AND   p.profName = p2.profName
AND   p.profLink = p2.profLink;