print("Welcome to a Simple LUA Calculator!")

local run = true
while run == true do
    io.write([[Please choose the number of the type of operation you wish to perform:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Percentage
        6. Exit
        ]])
    local op_fun = tonumber(io.read())

    if op_fun ~= 5 and op_fun ~= 6 and op_fun < 5 then
        io.write("Input first number: \n")
        Num1 = tonumber(io.read())
        io.write("Input second number: \n")
        Num2 = tonumber(io.read())
    elseif op_fun == 5 then
        io.write("Input the number to find its Percentage:\n")
        local percent_num = tonumber(io.read())
        io.write("Percentage to find:\n")
        local percentage = tonumber(io.read())
        local final_percentage = (percentage / 100) * percent_num
        print(percentage .. "% of " .. percent_num .. " is " .. final_percentage)
    end

    if op_fun == 1 then
        local add = Num1 + Num2
        print(Num1 .. " + " .. Num2 .. " = " .. add)
    elseif op_fun == 2 then
        local minus = Num1 - Num2
        print(Num1 .. " - " .. Num2 .. " = " .. minus)
    elseif op_fun == 3 then
        local multiply = Num1 * Num2
        print(Num1 .. " x " .. Num2 .. " = " .. multiply)
    elseif op_fun == 4 then
        if Num1 == 0 or Num2 == 0 then
            print("There was a mathematical error, Please try again")
        else
            local divide = Num1 / Num2
            print(Num1 .. " / " .. Num2 .. " = " .. divide)
        end
    elseif op_fun == 6 then
        print("Goodbye!")
        run = false
    else
        print("Invalid Choice, Please choose a valid operation.")
    end
end

