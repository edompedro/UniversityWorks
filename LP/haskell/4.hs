fToc :: Float -> Float
fToc f = (f - 32) * 5 / 9

main :: IO ()
main = do
  putStrLn "insira a temperatura em Fahrenheit:"
  f <- readLn
  let c = fToc f
  print (c)