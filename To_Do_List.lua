print([[
_______ ____    _____   ____    ___    _____   _____ _________ 
|__   __/ __ \  |  __ \ / __ \  | |    |_   _|/ ____|__   __|
   | | | |  | | | |  | | |  | | | |      | | | (___    | |   
   | | | |  | | | |  | | |  | | | |      | |  \___ \   | |   
   | | | |__| | | |__| | |__| | | |____ _| |_ ____) |  | |   
   |_|  \____/  |_____/ \____/  |______|_____|_____/   |_|   
   
   
   Welcome to a LUA To Do List!
   ----====================----
  
]])

local program = true

Table_List = {}

local function ViewList(tbl)
   print("------- LIST ------")
   for index, value in pairs(tbl) do
      print(index .. ". " .. value)
   end
   print("\n------------------\n")
end

local function AddList(tbl, t)
   return table.insert(tbl, t)
end

local function RemoveList(tbl, Task_Index)
   return table.remove(tbl, Task_Index)
end

while program do
   io.write([[
      Please choose what you want to do by typing the number of the task:
      1. View Current List
      2. Add Task to List
      3. Remove Task from List
      4. Clear List
      5. Exit
   ]])
   local operation = tonumber(io.read())

-- Exit

   if operation == 5 then
      print("\n------------------\n")
      program = false
      print("Goodbye!")
   end

-- -- View To Do List, If empty, returns a statement

   if operation == 1 then
      if next(Table_List) == nil then
         print("The list is currently empty, You have no pending task!")
         print("\n------------------\n")
      else
         ViewList(Table_List)
      end
   end

-- Adding Task to List, Secondary Loop to continue adding Task, View List or Exit out to main loop

   if operation == 2 then
      print("\n------------------\n")
         io.write("Please add a task to the list.. \n")
         Task = io.read()
         AddList(Table_List, Task)
         print("Your task has been added!")
         print("Updated List is:")
         ViewList(Table_List)
   end

-- Remove Task from list
   if operation == 3 then
      print("\n------------------\n")
         io.write("Please type the number of the task that needs to be removed.. \n")
         Task_Index = tonumber(io.read())
         RemoveList(Table_List, Task_Index)

         print("Your task has been removed!")
         print("Updated List is:")
         ViewList(Table_List)
   end

   if operation == 4 then
      Table_List = {}
      print("\n------------------\n")
      print("List has been cleared successfully")
   end
end
