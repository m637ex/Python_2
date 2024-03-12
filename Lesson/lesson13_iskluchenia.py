'''
Исключения!!! конспект


!!!Команда try
!!!Команда except
!!!Команда finally
Блок finally выполняется в любом случае
 ...
 try:
 # отлавливаем ошибки
 ...
 except NameError as e:
 # действия при перехвате ошибки NameError
 ...
 else:
 # Дополнительные действия можно указать в блоке else. не сработает, если есть исключение, return, break? или continue
 ...
 finally:
 # выполняется в любом случае
 ...
 # продолжаем нормальную работу
 ...
 
!!!Команда else
Дополнительные действия можно указать в блоке else.
Блок else не сработает, если внутри try произошло любое из событий:
возбуждено исключение
выполнена команда return
выполнена команда break
выполнена команда continue


!!!Иерархия исключений
— Exception
    Arithmetic€rror
        FloatingPointError
        OverflowError
        ZeroDivisionError
    AssertionError
    Attributetrror
    BufferError
    €0FError
    ExceptionGroup [BaseExceptionGroup]
    ImportError
        ModuleNotFoundError
    LookupError
        IndexError
        KeyError
    MemoryError
    NameError
        UnboundLocalError
    OSError
        BlockinglOError 
        ChildProcessError 
        ConnectionError
            BrokenPipeError
            ConnectionAbortedError
            ConnectionRefusedError
            ConnectionResetError 
        FileExistsError 
        FileNotFoundError 
        InterruptedError 
        IsADirectoryError 
        NotADirectoryError 
        PermissionError 
        ProcessLookupError 
        TimeoutError
    ReferenceError
    RuntimeError
        NotImplementedError
        RecursionError
    StopAsyncIteration
    StopIteration
    SyntaxError
        IndentationError
            TabError
    SystemError
    TypeError
    ValueError
        UnicodeError
            UnicodeDecodeError
            UnicodeEncodeError
            UnicodeTranslateError
    Warning
        BytesWarning
        DeprecationWarning
        EncodingWarning
        FuturewWarning
        ImportWarning
        PendingDeprecationWarning
        ResourceWarning
        RuntimeWarning
        SyntaxWarning
        UnicodewWarning
        UserWarning

!!!Ключевое слово raise

Создание собственных исключений
Разработчик может создавать свои классы исключения
● Исключение не должно дублировать стандартное исключение
● Собственные исключения наследуются от класса Exception
○ Если исключений несколько, создают собственное
родительское исключение от Exception. Остальные
исключения наследуются от него.
● Для исключения достаточно определить два дандер метода:
○ __init__
○ __str__




'''