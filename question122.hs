import Control.Monad.State
import Data.List (minimumBy)
import Data.Ord (comparing)
import Data.Maybe (listToMaybe, mapMaybe)
import qualified Data.Sequence as Seq
import Data.Foldable (toList)

-- Define the State type alias for convenience
type Counter = State Int

-- Define the data type for a general tree with each node containing a value and an array of numbers, and branches having weights
data Tree a = Node a [Int] [(Tree a, Int)]
            deriving (Show, Eq)

-- Function to add a weighted child to a specific node in a general tree
addChild :: (Eq a) => a -> a -> [Int] -> Int -> Tree a -> Tree a
addChild target val arr weight (Node a nums children)
    | a == target = Node a nums (children ++ [(Node val arr [], weight)])
    | otherwise = Node a nums (map (\(child, w) -> (addChild target val arr weight child, w)) children)

-- Function to add new nodes to leaf nodes for each number in their array, with a stopping condition
addNumbersAsBranchesToLeafs :: Int -> Tree Int -> Tree Int
addNumbersAsBranchesToLeafs stopNum (Node a nums children)
    | a >= stopNum = Node a nums children  -- Stop if the current node's value is equal to or greater than the stopping number
    | null children = Node a nums (map (\num -> (Node (a + num) (nums ++ [a + num]) [], 0)) nums)  -- If it's a leaf node, add new nodes for each number in the array
    | otherwise = Node a nums (map (\(child, weight) -> (addNumbersAsBranchesToLeafs stopNum child, weight)) children)

-- The applyNTimes function modified to use the State monad to track applications
applyNTimes :: Int -> (a -> a) -> a -> Counter a
applyNTimes 0 _ x = return x
applyNTimes n f x = do
    modify (+1)  -- Increment the counter
    applyNTimes (n - 1) f (f x)

-- Function to run the state and get the final count along with the result
applyNTimesWithCount :: Int -> (a -> a) -> a -> (a, Int)
applyNTimesWithCount n f x = runState (applyNTimes n f x) 0

-- DFS function to find the first encounter of a number in the tree
dfsFindFirst :: (Eq a) => a -> Tree a -> Maybe (Tree a)
dfsFindFirst target (Node a nums children)
    | a == target = Just (Node a nums children)
    | otherwise = listToMaybe $ mapMaybe (dfsFindFirst target . fst) children

bfsFindFirst :: (Eq a) => a -> Tree a -> Maybe (Tree a)
bfsFindFirst target root = bfsHelper (Seq.singleton root)
  where
    bfsHelper Seq.Empty = Nothing
    bfsHelper (Node a nums children Seq.:<| queue)
        | a == target = Just (Node a nums children)
        | otherwise = bfsHelper (queue Seq.>< Seq.fromList (map fst children))

-- Main function to test the tree operations
main :: IO ()
main = do
    let tree = Node 1 [1]
                [ (Node 2 [1,2] [], 1)
                ]

    let stopNum = 200  -- Define the stopping number
    let addNumbers = addNumbersAsBranchesToLeafs stopNum
    let (result_tree, count) = applyNTimesWithCount 10 addNumbers tree
    print count

    let target = 200
    let result = bfsFindFirst target result_tree
    print result