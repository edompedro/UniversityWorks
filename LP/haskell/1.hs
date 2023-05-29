main :: IO ()
potenciacao :: (Num a, Integral b) => a -> b -> a
potenciacao x n
  | n == 0    = 1
  | otherwise = x * potenciacao x (n - 1)
main = return ()