
select S1.Id, S1.Score, count(*) as Rank
  from Scores as S1
  outer join (
    select distinct(Score) as Score from Score
  ) as S2
  on S1.Score <= S2.Score
  group by S1.Id,
  order by S1.Score desc, S1.Id asc
